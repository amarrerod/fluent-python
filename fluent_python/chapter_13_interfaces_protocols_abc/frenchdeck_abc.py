#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   frenchdeck_abc.py
@Time    :   2023/12/11 10:14:06
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2023, Alejandro Marrero
@Desc    :   None
"""

from collections import namedtuple, abc

Card = namedtuple("Card", ["rank", "suit"])

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    """
    Function to order the deck in order of increasing rank
    """
    rank_value = FrenchDeck2.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


class FrenchDeck2(abc.MutableSequence):
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, value):
        self._cards[position] = value

    def __delitem__(self, position):
        del self._cards[position]

    def insert(self, position, value):
        self._cards.insert(position, value)
