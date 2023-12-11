#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   tombolist.py
@Time    :   2023/12/11 11:17:01
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2023, Alejandro Marrero
@Desc    :   None
"""

from random import randrange
from .tombola import Tombola


@Tombola.register
class Tombo(list):
    def pick(self):
        if self:
            position = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError("pop from an empty Tombo")

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(self)
