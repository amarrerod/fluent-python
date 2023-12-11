#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   bingo.py
@Time    :   2023/12/11 11:03:31
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2023, Alejandro Marrero
@Desc    :   None
"""

from .tombola import Tombola
import random


class Bingo(Tombola):
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError("pick from an empty Bingo")

    def __call__(self):
        self.pick()

    def loaded(self):
        return bool(self._items)

    def inspect(self):
        return tuple(self._items)
