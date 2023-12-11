#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   tombola.py
@Time    :   2023/12/11 10:53:09
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2023, Alejandro Marrero
@Desc    :   None
"""

import abc


class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self, iterable):
        """Add items from an iterable"""

    @abc.abstractmethod
    def pick(self):
        """Removes an item at random, returning it.
        This method should raise 'LookupError' when the instance is empty
        """

    def loaded(self):
        """Return `True` if there's at least 1 item, `False` otherwise"""
        return bool(self.inspect())

    def inspect(self):
        """Return a sorted tuple with the items currently inside"""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(items)
