#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   proc_pol.py
@Time    :   2024/07/02 10:41:29
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2024, Alejandro Marrero
@Desc    :   None
'''

import sys
from concurrent import futures
from time import perf_counter
from typing import NamedTuple

from primes import NUMBERS, is_prime


class PrimeResult(NamedTuple):
    n: int
    flag: bool
    elapsed: float

def check(n: int) -> PrimeResult:
    t0 = perf_counter()
    res = is_prime(n)
    return PrimeResult(n, res, perf_counter() - t0)

def main():
    if len(sys.argv) < 2:
        workers = None

    else:
        workers = int(sys.argv[1])

    executor = futures.ProcessPoolExecutor(workers)
    actual_workers = executor._max_workers
    print(f'Checking  {len(NUMBERS)} numbers with {actual_workers} processes.')
    t0 = perf_counter()
    numbers = sorted(NUMBERS, reverse=True)
    with executor:
        for n, prime, elapsed in executor.map(check, numbers):
            label = 'P' if prime else ' '
            print(f'{n:16}  {label}  {elapsed:9.6f}s')
    time = perf_counter() - t0
    print(f'Total time: {time:.2f}s')

if __name__ == '__main__':
    main()