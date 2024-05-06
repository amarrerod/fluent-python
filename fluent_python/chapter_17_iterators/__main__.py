#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   __main__.py
@Time    :   2024/05/06 09:28:36
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2024, Alejandro Marrero
@Desc    :   None
"""

from .sentence_gen_exp import Sentence
from .ar_progression import ArithmeticProgression, aritprog_gen, aritprog_gen_itertools
import random
from fractions import Fraction
from decimal import Decimal
import itertools


def die():
    return random.randint(1, 6)


def main():
    s = Sentence('"The time has come", the Walrus said,')
    print(s)
    for word in s:
        print(word)
    print(list(s))

    d_6_iter = iter(die, 1)
    print(d_6_iter)
    for roll in d_6_iter:
        print(roll)

    ap = ArithmeticProgression(0, 1, 3)
    print(list(ap))
    ap = ArithmeticProgression(1, 0.5, 3)
    print(list(ap))
    ap = ArithmeticProgression(0, 1 / 3, 1)
    print(list(ap))
    ap = ArithmeticProgression(0, Fraction(1, 3), 1)
    print(list(ap))
    ap = ArithmeticProgression(0, Decimal(".1"), 0.3)
    print(list(ap))

    ap = aritprog_gen(0, 1, 3)
    print(list(ap))
    ap = aritprog_gen(1, 0.5, 3)
    print(list(ap))
    ap = aritprog_gen(0, 1 / 3, 1)
    print(list(ap))
    ap = aritprog_gen(0, Fraction(1, 3), 1)
    print(list(ap))
    ap = aritprog_gen(0, Decimal(".1"), 0.3)
    print(list(ap))

    ap = itertools.count(0, 0.5)
    ap = itertools.takewhile(lambda n: n < 3, itertools.count(1, 0.5))
    print(list(ap))

    ap = aritprog_gen_itertools(0, 1, 3)
    print(list(ap))
    ap = aritprog_gen_itertools(1, 0.5, 3)
    print(list(ap))
    ap = aritprog_gen_itertools(0, 1 / 3, 1)
    print(list(ap))
    ap = aritprog_gen_itertools(0, Fraction(1, 3), 1)
    print(list(ap))
    ap = aritprog_gen_itertools(0, Decimal(".1"), 0.3)
    print(list(ap))


if __name__ == "__main":
    main()
