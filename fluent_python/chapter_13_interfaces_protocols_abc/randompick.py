#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   randompick.py
@Time    :   2023/12/12 09:59:26
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2023, Alejandro Marrero
@Desc    :   None
"""


from typing import Protocol, runtime_checkable, Any


@runtime_checkable
class RandomPicker(Protocol):
    def pick(self) -> Any:
        ...
