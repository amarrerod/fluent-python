import pytest

from fluent_python.chapter_3_dicts_and_sets.__main__ import get_creators
from fluent_python.chapter_3_dicts_and_sets.str_key_dict import StrKeyDict
from collections import OrderedDict


def test_dict_mappings():
    b1 = dict(
        api=1, author="Douglas Hofstadter", type="book", title="Gödel, Escher, Bach"
    )
    creator = get_creators(b1)
    expected = ["Douglas Hofstadter"]
    assert creator == expected


def test_dict_mappings_with_order():
    b2 = OrderedDict(
        api=2,
        type="book",
        title="Python in a Nutshell",
        authors="Martelli Ravenscroft Holden".split(),
    )

    expected = ["Martelli", "Ravenscroft", "Holden"]
    creator = get_creators(b2)
    assert creator == expected


def test_dict_raises():
    r = {"type": "book", "pages": 770}
    with pytest.raises(ValueError) as excep:
        get_creators(r)

    assert str(excep.value) == f"Invalid book record: {r!r}"


def test_custom_dict():
    d = StrKeyDict([("2", "two"), ("4", "four")])
    assert d["2"] == "two"
    assert d[4] == "four"

    with pytest.raises(KeyError) as excep:
        d[1]
    assert str(excep.value) == f"'1'"
