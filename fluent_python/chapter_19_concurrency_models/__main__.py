#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   __main__.py
@Time    :   2024/05/22 09:31:40
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2024, Alejandro Marrero
@Desc    :   None
"""

from .spinner_thread import supervisor as sup_thread
from .spinner_process import supervisor as sup_process
from .spinner_async import main as sup_async


def main():
    result = sup_thread()
    print(f"Answer: {result}")

    result = sup_process()
    print(f"Answer: {result}")

    sup_async()


if __name__ == "__main__":
    main()
