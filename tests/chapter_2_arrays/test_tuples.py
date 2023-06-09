import pytest

from fluent_python.chapter_2_arrays.__main__ import fixed_size


@pytest.fixture
def immutable():
    return (10, "alpha", (1, 2))


@pytest.fixture
def mutable():
    return (10, "alpha", [1, 2])


def test_hashable_tuples(immutable, mutable):
    assert fixed_size(immutable)
    assert not fixed_size(mutable)
