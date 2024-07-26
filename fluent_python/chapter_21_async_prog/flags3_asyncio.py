#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   flags3_asyncio.py
@Time    :   2024/07/26 09:50:54
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2023, Alejandro Marrero
@Desc    :   None
"""


import asyncio
from collections import Counter
from http import HTTPStatus
from pathlib import Path

import httpx
import tqdm

from flags_2_common import main, DownloadStatus, save_flag

DEFAULT_CONCUR_REQ = 5
MAX_CONCUR_REQ = 1000


async def get_country(client: httpx.AsyncClient, base_url: str, cc: str) -> str:
    url = f"{base_url}/{cc}/metadata.json".lower()
    response = await client.get(url, timeout=3.1, follow_redirects=True)
    response.raise_for_status()
    metadata = response.json()
    return metadata["country"]


async def get_flag(client: httpx.AsyncClient, base_url: str, cc: str) -> bytes:
    url = f"{base_url}/{cc}/{cc}.gif".lower()
    response = await client.get(url, timeout=3.1, follow_redirects=True)
    response.raise_for_status()
    return response.content


async def download_one(
    client: httpx.AsyncClient,
    cc: str,
    base_url: str,
    semaphore: asyncio.Semaphore,
    verbose: bool,
) -> DownloadStatus:
    try:
        async with semaphore:
            image = await get_flag(client, base_url, cc)
        async with semaphore:
            country = await get_country(client, base_url, cc)
    except httpx.HTTPStatusError as exc:
        response = exc.response
        if response.status_code == HTTPStatus.NOT_FOUND:
            status = DownloadStatus.NOT_FOUND
            msg = f"not found: {response.url}"
        else:
            raise
    else:
        filename = country.replace(" ", "_")
        await asyncio.to_thread(save_flag, image, f"{filename}.gif")
        status = DownloadStatus.OK
        msg = "OK"
    if verbose and msg:
        print(cc, msg)
    return status


async def supervisor(
    cc_list: list[str], base_url: str, verbose: bool, concur_req: int
) -> Counter[DownloadStatus]:
    counter: Counter[DownloadStatus] = Counter()
    semaphore = asyncio.Semaphore(concur_req)
    async with httpx.AsyncClient() as client:
        to_do = [
            download_one(client, cc, base_url, semaphore, verbose) for cc in cc_list
        ]
        to_do_iter = asyncio.as_completed(to_do)
        if not verbose:
            to_do_iter = tqdm.tqdm(to_do_iter, total=len(cc_list))
        error: httpx.HTTPError | None = None
        for coro in to_do_iter:
            try:
                status = await coro
            except httpx.HTTPStatusError as exc:
                error_msg = (
                    "HTTP error {response.status_code} - {response.reason_phrase}"
                )
                error_msg = error_msg.format(reponse=exc.response)
                error = exc
            except httpx.RequestError as exc:
                error_msg = f"{exc} {type(exc)}".strip()
                error = exc
            except KeyboardInterrupt:
                break

            if error:
                status = DownloadStatus.ERROR
                if verbose:
                    url = str(error.request.url)
                    cc = Path(url).stem.upper()
                    print(f"{cc} error: {error_msg}")

            counter[status] += 1
    return counter


def download_many(
    cc_list: list[str], base_url: str, verbose: bool, concur_req: int
) -> Counter[DownloadStatus]:
    coro = supervisor(cc_list, base_url, verbose, concur_req)
    counts = asyncio.run(coro)
    return counts


if __name__ == "__main__":
    main(download_many, DEFAULT_CONCUR_REQ, MAX_CONCUR_REQ)
