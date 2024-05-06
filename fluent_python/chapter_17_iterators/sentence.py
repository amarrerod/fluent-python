#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   sequence.py
@Time    :   2024/05/06 09:33:12
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
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        if index < 0 or index > len(self.words):
            raise RuntimeError(
                f"Trying to access a word that does not exists. Index {index} and len(words) = {len(self.words)}"
            )
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return "Sentence(%s)" % reprlib.repr(self.text)
