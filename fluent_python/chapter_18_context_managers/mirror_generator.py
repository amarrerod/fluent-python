#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   mirror_generator.py
@Time    :   2024/05/20 14:16:31
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2024, Alejandro Marrero
@Desc    :   None
"""


import contextlib
import sys


@contextlib.contextmanager
def looking_glass():
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    msg = ""
    try:
        yield "JABBERWOCKY"
    except ZeroDivisionError:
        msg = "Please DO NOT divide by zero!"
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)
