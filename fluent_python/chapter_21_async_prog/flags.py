#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   flags.py
@Time    :   2024/06/05 14:31:25
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2024, Alejandro Marrero
@Desc    :   None
"""


import time
from pathlib import Path
from typing import Callable

import httpx

POP20_CC = ("CN IN US ID BR PK NG BD RU JP MX PH VN ET EG DE IR TR CD FR").split()
BASE_URL = "https://www.fluentpython.com/data/flags"
DEST_DIR = Path("downloaded")


def save_flag(img: bytes, filename: str) -> None:
    (DEST_DIR / filename).write_bytes(img)


async def get_flag(client: httpx.AsyncClient, cc: str) -> bytes:
    url = f"{BASE_URL}/{cc}/{cc}.gif".lower()
    resp = await client.get(url, timeout=6.1, follow_redirects=True)
    return resp.read()


async def download_one(client: httpx.AsyncClient, cc: str):
    image = await get_flag(client, cc)
    save_flag(image, f'{cc}.gif')
    print(cc, end=' ', flush=True)
    return cc

def main(downloader: Callable[[list[str]], int]):
    DEST_DIR.mkdir(exist_ok=True)
    t0 = time.perf_counter()
    count = downloader(POP20_CC)
    elapsed = time.perf_counter() - t0
    print(f"\n{count} downloads in {elapsed:.2f}s")