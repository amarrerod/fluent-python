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
    with futures.ThreadPoolExecutor() as executor:
        res = executor.map(download_one, sorted(cc_list))

    return len(list(res))


if __name__ == "__main__":
    main(download_many)
