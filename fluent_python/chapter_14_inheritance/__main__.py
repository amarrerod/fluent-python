#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   __main__.py
@Time    :   2023/12/13 09:13:18
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2023, Alejandro Marrero
@Desc    :   None
"""

from .uppermixin import UpperDict, UpperCounter


def main():
    d = UpperDict([("a", "letter A"), ("2", "digit two")])
    print(d)
    d["b"] = "letter B"
    print(d)
    print(f'Is the letter b in d: {"b" in d}')

    c = UpperCounter("BaNanAs")
    print(c.most_common())


if __name__ == "__main__":
    main()
