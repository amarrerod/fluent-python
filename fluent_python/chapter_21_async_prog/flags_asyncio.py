#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   flags_asyncio.py
@Time    :   2024/07/19 11:48:16
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2024, Alejandro Marrero
@Desc    :   None
'''
import asyncio

import httpx
from flags import download_one, main


def download_many(cc_list: list[str]) -> int:
    return asyncio.run(supervisor(cc_list))

async def supervisor(cc_list: list[str]) -> int:
    async with httpx.AsyncClient() as client:
        to_do = [download_one(client, cc) for cc in sorted(cc_list)]
        result = await asyncio.gather(*to_do)
    
    return len(result)
        

if __name__ == "__main__":
    main(download_many)