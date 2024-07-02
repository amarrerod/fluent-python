#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   flags_threadpool.py
@Time    :   2024/06/05 14:43:19
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2024, Alejandro Marrero
@Desc    :   None
"""


from concurrent import futures

from flags import get_flag, main, save_flag


def download_one(cc: str):
    image = get_flag(cc)
    save_flag(image, f"{cc}.gif")
    print(cc, end=" ", flush=True)
    return cc


def download_many(cc_list: list[str]) -> int:
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do : list[futures.Future] = []
        for cc in sorted(cc_list):
            future = executor.submit(download_one, cc)
            to_do.append(future)
            print(f'Scheduled for {cc}: {future!r}')
        
        for count, future, in enumerate(futures.as_completed(to_do), 1):
            res: str = future.result()
            print(f'{future} result: {res!r}')
    return count

if __name__ == "__main__":
    main(download_many)
