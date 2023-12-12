#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   double_protocol.py
@Time    :   2023/12/12 09:48:29
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2023, Alejandro Marrero
@Desc    :   None
"""

from typing import TypeVar, Protocol

T = TypeVar("T")


class Repeatable(Protocol):
    def __mul__(self: T, repeat_count: int) -> T:
        ...


RT = TypeVar("RT", bound=Repeatable)


def double(x: RT) -> RT:
    return x * 2
