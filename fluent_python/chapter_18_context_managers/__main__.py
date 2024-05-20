#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   __main__.py
@Time    :   2024/05/20 14:15:29
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2024, Alejandro Marrero
@Desc    :   None
"""

from .mirror_generator import looking_glass


def evaluate(item):
    match item:
        case ["hello", x]:
            return x

        case ("hello", x):
            return x

        case {"hello": 1, **x}:
            return x

        case [{"hello": 1}, x]:
            return x
        case _:
            return "No match found"


def main():
    with looking_glass() as what:
        print("Alice, Kitty and Snowdrop")
        print(what)

    print(what)

    x = evaluate(["hello", list(range(10))])
    print(x)
    x = evaluate(("hello", tuple(range(10))))
    print(x)
    x = evaluate({"hello": 1, "other": list(range(10))})
    print(x)
    x = evaluate([{"hello": 1}, list(range(10))])
    print(x)


if __name__ == "__main__":
    main()
