#!/usr/bin/env python

"""Tests for `fluent_python` package."""

import pytest


from fluent_python.chapter_1_data_model.euclidean_vector import Vector


def test_vector_add():
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)
    expected = Vector(4, 5)
    assert v1 + v2 == expected


def test_vector_abs():
    v = Vector(3, 4)
    # Calculates the magnitude of a vector
    expected = 5.0
    assert abs(v) == expected


def test_vector_multiplication():
    v = Vector(3, 4)
    expected = Vector(9, 12)
    assert v * 3 == expected


def test_vector_mult_magn():
    v = Vector(3, 4)
    expected = 15.0
    assert abs(v * 3) == expected
