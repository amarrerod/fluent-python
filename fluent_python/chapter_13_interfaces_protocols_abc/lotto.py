#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   lotto.py
@Time    :   2023/12/11 11:11:05
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2023, Alejandro Marrero
@Desc    :   None
"""

from .tombola import Tombola
import random


class Lotto(Tombola):
    def __init__(self, iterable):
        self._balls = list(iterable)

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError("pick from an empty Lotto")
        return self._balls.pop(position)

    def loaded(self):
        return bool(self._balls)

    def inspect(self):
        return tuple(self._balls)
