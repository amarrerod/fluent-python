#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   sentence_gen_exp.py
@Time    :   2024/05/06 10:36:39
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2024, Alejandro Marrero
@Desc    :   None
"""

import re
import reprlib

RE_WORD = re.compile(r"\w+")


class Sentence:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return f"Sentence({reprlib.repr(self.text)})"

    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text))
