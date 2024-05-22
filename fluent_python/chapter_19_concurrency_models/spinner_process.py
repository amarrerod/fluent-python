#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   spinner_process.py
@Time    :   2024/05/22 10:30:15
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2024, Alejandro Marrero
@Desc    :   None
"""

import itertools
import time
from multiprocessing import Process, Event, synchronize
from .primes import is_prime


def spin(msg: str, done: synchronize.Event) -> None:
    for char in itertools.cycle(r"\|/-"):
        status = f"\r{char} {msg}"
        print(status, end="", flush=True)
        if done.wait(0.1):
            break
    blanks = " " * len(status)
    print(f"\r{blanks}\r", end="")


def slow() -> int:
    # time.sleep(3)
    n = 5_000_111_000_222_021
    is_prime(n)
    return 42


def supervisor() -> int:
    done = Event()
    spinner = Process(target=spin, args=("thinking!", done))
    print(f"Spinner object: {spinner}")
    spinner.start()
    result = slow()
    done.set()
    spinner.join()
    return result
