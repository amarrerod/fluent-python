#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   flags_2_sequential.py
@Time    :   2024/07/03 08:34:49
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2024, Alejandro Marrero
@Desc    :   None
'''

from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed

import httpx
import tqdm
from flags_2_common import DownloadStatus, main
from flags_2_sequential import download_one

DEFAULT_CONCUR_REQ = 30
MAX_CONCUR_REQ = 1000


def download_many(cc_list: list[str], base_url : str, verbose: bool, concur_red: int) -> Counter[DownloadStatus]:
    counter: Counter[DownloadStatus] = Counter()
    with ThreadPoolExecutor(max_workers=concur_red) as executor:
        to_do_map = {}
        for cc in sorted(cc_list):
            future = executor.submit(download_one, cc, base_url, verbose)
            to_do_map[future] = cc

        done_iter = as_completed(to_do_map)
        if not verbose:
            done_iter = tqdm.tqdm(done_iter, total=len(cc_list))
        
        for future in done_iter:
            try:
                status = future.result()
            except httpx.HTTPStatusError as exc:
                error_msg = 'HTTP error {resp.status_code} - {resp.reason_phrase}'
                error_msg = error_msg.format(resp=exc.response)
            except httpx.RequestError as exc:
                error_msg = f'{exc} {type(exc)}'.strip()
            except KeyboardInterrupt:
                break
            else:
                error_msg = ''
            
            if error_msg:
                status = DownloadStatus.ERROR
            counter[status] += 1
            if verbose and error_msg:
                cc = to_do_map[future]
                print(f'{cc} error: {error_msg}')
    return counter

if __name__ == '__main__':
    main(download_many, DEFAULT_CONCUR_REQ, MAX_CONCUR_REQ)