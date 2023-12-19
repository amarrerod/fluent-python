#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   uppermixin.py
@Time    :   2023/12/13 09:14:24
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2023, Alejandro Marrero
@Desc    :   None
"""


import collections


def _upper(key):
    try:
        return key.upper()
    except AttributeError:
        return key


class UpperCaseMixin:
    def __setitem__(self, key, value):
        super().__setitem__(_upper(key), value)

    def __getitem__(self, key):
        super().__getitem__(_upper(key))

    def get(self, key, default=None):
        return super().get(_upper(key), default)

    def __contains__(self, key):
        return super().__contains__(_upper(key))


class UpperDict(UpperCaseMixin, collections.UserDict):
    """Specialized 'Dict' class that uppercases string keys"""


class UpperCounter(UpperCaseMixin, collections.Counter):
    """Specialized 'Counter' class that uppercases string keys"""
