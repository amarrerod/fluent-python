#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   tree.py
@Time    :   2024/05/17 11:05:55
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2023, Alejandro Marrero
@Desc    :   None
"""


def tree(cls, level=0):
    yield cls.__name__, level  # Name and indentation
    for sub_cls in cls.__subclasses__():
        yield from tree(sub_cls, level + 1)


def sub_tree(cls, level):
    for sub_cls in cls.__subclasses__():
        yield sub_cls.__name__, level
        # Replace a nested for loop to iterate over the following N levels
        # by using a yield from on the same generator
        # we include the level parameter to allow the recursion to work properly
        yield from sub_tree(sub_cls, level + 1)


def display(cls):
    for cls_name, level in tree(cls):
        indent = " " * 4 * level
        print(f"{indent}{cls_name}")


if __name__ == "__main__":
    display(BaseException)
