#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   demo_executor_map.py
@Time    :   2024/07/02 10:51:38
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2024, Alejandro Marrero
@Desc    :   None
'''

from concurrent import futures
from time import sleep, strftime


def display(*args):
    print(strftime('[%H:%M:%S]'), end=' ')
    print(*args)

def loiter(n):
    msg = '{}loiter({}): doing nothing for {}s...'
    display(msg.format('\t'*n, n,n))
    sleep(n)
    msg = '{}loiter({}): done.'
    display(msg.format('\t'*n, n))
    return n * 10

def main():
    display('Script starting.')
    executor = futures.ThreadPoolExecutor(max_workers=3)
    results = executor.map(loiter, range(10))
    display('results: ', results)
    display('Waiting for individual results:')
    for i, result in enumerate(results):
        display(f'result {i}: {result}')

if __name__ == '__main__':
    main()