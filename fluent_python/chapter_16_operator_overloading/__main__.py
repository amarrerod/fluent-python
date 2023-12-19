#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   __main__.py
@Time    :   2023/12/19 09:29:34
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2023, Alejandro Marrero
@Desc    :   None
"""

from .vector import Vector


def main():
    v1 = Vector(list(range(10)))
    v2 = v1 + tuple(range(5, 10))
    print(f"V1 is: {v1} and v2 is: {v2}")
    v3 = list(range(10, 50)) + v2
    print(f"V3 is: {v3}")

    v4 = v1 * 5
    print(f"V1 is: {v1} and v4 is: {v4}")

    va = Vector([1, 2, 3])
    vz = Vector([5, 6, 7])
    vx = va @ vz
    print(f"Va is: {va}, Vz is: {vz} and Va @ Vz is: {vx}")


if __name__ == "__main__":
    main()
