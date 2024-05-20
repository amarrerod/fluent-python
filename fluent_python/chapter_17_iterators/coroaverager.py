#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   coroaverager.py
@Time    :   2024/05/17 11:22:51
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2023, Alejandro Marrero
@Desc    :   None
"""

from collections.abc import Generator
from typing import NamedTuple, TypeAlias


def averager() -> Generator[float, float, None]:
    total = 0.0
    count = 0
    average = 0.0
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


# New version that does not yield partial results
# instead, it returns a tuple with the number of terms and the average
class Result(NamedTuple):
    count: int
    average: float


class Sentinel:
    def __repr__(self):
        return "<Sentinel>"


STOP = Sentinel()
SendType: TypeAlias = float | Sentinel


def averager_2(verbose: bool = False) -> Generator[None, SendType, Result]:
    total = 0.0
    count = 0
    average = 0.0
    while True:
        term = yield
        if verbose:
            print(f"Received: {term}")
        if isinstance(term, Sentinel):
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)


def compute():
    result = yield from averager_2(True)
    print(f"The computed result is: {result}")
    return result
