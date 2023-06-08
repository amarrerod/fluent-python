#!/usr/bin/env python

"""Tests for `fluent_python` package."""

import pytest


from fluent_python.chapter_1_data_model.card_deck import Card, FrenchDeck


@pytest.fixture
def deck():
    return FrenchDeck()


def test_card_in(deck):
    q_hearts = Card("Q", "hearts")
    assert q_hearts in deck


def test_card_no_in(deck):
    false_card = Card("7", "beasts")
    assert false_card not in deck


def test_len_method(deck):
    assert len(deck) == 52


def test_slicing(deck):
    expected = Card("A", "hearts")
    assert deck[-1] == expected


def test_only_aces(deck):
    assert all(c.rank == "A" for c in deck[12::13])
