#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   ar_progression.py
@Time    :   2024/05/06 10:44:40
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2024, Alejandro Marrero
@Desc    :   None
"""

import itertools


class ArithmeticProgression:

    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end  # None -> 'infinite' series

    def __iter__(self):
        # Get the type of adding self.begin and self.step. For
        # example, if one is int and the other is float, result_type
        # will be a float
        result_type = type(self.begin + self.step)
        # This line makes a result with the same numeric value
        # of self.begin, but coerced to the type of the subsequent additions
        result = result_type(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index


def aritprog_gen(begin, step, end=None):
    # Get the type of adding begin and step. For
    # example, if one is int and the other is float, result_type
    # will be a float
    result_type = type(begin + step)
    # This line makes a result with the same numeric value
    # of begin, but coerced to the type of the subsequent additions
    result = result_type(begin)
    forever = end is None
    index = 0
    while forever or result < end:
        yield result
        index += 1
        result = begin + step * index


def aritprog_gen_itertools(begin, step, end=None):
    # Get the type of adding begin and step. For
    # example, if one is int and the other is float, result_type
    # will be a float
    first = type(begin + step)(begin)
    ap_gen = itertools.count(first, step)
    if end is None:
        return ap_gen
    return itertools.takewhile(lambda n: n < end, ap_gen)
