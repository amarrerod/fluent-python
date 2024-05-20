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
from .coroaverager import averager, averager_2, STOP, compute


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

    # Chain from iterable example
    text = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    r = list(itertools.chain.from_iterable(enumerate(text)))
    print(r)
    r = list(itertools.chain(enumerate(text)))
    print(r)

    rows = itertools.product(text[:3], range(2), repeat=3)
    for r in rows:
        print(r)

    combs = itertools.combinations(text[:10], 4)
    for c in combs:
        print(c)

    combs = itertools.combinations_with_replacement(text[:10], 4)
    for c in combs:
        print(c)

    pairs = itertools.pairwise(text[:10])
    for c in pairs:
        print(c)

    permu = itertools.permutations(text[:3])
    for c in permu:
        print(c)

    coro_avg = averager()
    print(next(coro_avg))  # Priming the coroutine
    for i in [10, 30, 5]:
        print(coro_avg.send(i))

    coro_avg = averager_2()
    next(coro_avg)  # Priming the coroutine
    for i in [10, 30, 6.5]:
        # It wont show anything because the coroutine does not yield partial results
        print(coro_avg.send(i))
    coro_avg.close()

    coro_avg = averager_2()
    next(coro_avg)  # Priming the coroutine
    for i in [10, 30, 6.5]:
        # It wont show anything because the coroutine does not yield partial results
        print(coro_avg.send(i))

    try:
        coro_avg.send(STOP)
    except StopIteration as exc:
        result = exc.value

    print(f"The result is: {result}")

    comp = compute()
    for v in [None, 10, 20, 30, STOP]:
        try:
            comp.send(v)
        except StopIteration as exc:
            r = exc.value
    print(f"Result is {r}")


if __name__ == "__main":
    main()
