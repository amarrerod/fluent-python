""" Chapter 3 examples"""

from collections import defaultdict
import random


def dict_comp():
    dial_codes = [
        (880, "Bangladesh"),
        (55, "Brazil"),
        (86, "China"),
        (91, "India"),
        (62, "Indonesia"),
        (81, "Japan"),
        (234, "Nigeria"),
        (92, "Pakistan"),
        (7, "Russia"),
        (1, "United States of America"),
    ]

    country_dial = {country: code for code, country in dial_codes}
    print(f"Country Dials: {country_dial}")

    country_dial_upper = {
        code: country.upper()
        for country, code, in sorted(country_dial.items())
        if code < 70
    }
    print(f"Country codes with code as keys: {country_dial_upper}")


def __dump_fn(**kwargs):
    return kwargs


def unpacking_mappings():
    result = __dump_fn(**{"x": 1}, y=2, **{"z": 3})
    print(f"Result is: {result}")


def merging_mappings():
    d1 = {"a": 1, "b": 3}
    d2 = {"a": 2, "b": 4, "c": 6}
    d3 = d1 | d2
    print(f"D1: {d1}, D2: {d2}, D3: {d3}")
    d1 |= d2
    print(f"Updating D1: {d1}")


def get_creators(record: dict) -> list:
    match record:
        case {"type": "book", "api": 2, "authors": [*names]}:
            return names

        case {"type": "book", "api": 1, "author": name}:
            return [name]

        case {"type": "book"}:
            raise ValueError(f"Invalid book record: {record!r}")

        case {"type": "movie", "director": name}:
            return [name]

        case _:
            raise ValueError(f"Invalid record: {record!r}")


def match_extra():
    food = dict(category="ice cream", flavour="vanilla", cost=199)
    match food:
        case {"category": "ice cream", **details}:
            print(f"Ice cream detailts: {details}")


def default_dicts():
    # default dict of lists
    dd = defaultdict(list)

    print(f'Default example: {dd["example"]}')


def dict_views():
    d = dict(a=10, b=20, c=30)

    print(f"Values of d: {d.values()}")
    print(f"Len of values: {len(d.values())}")
    l = list(d.values())
    print(f"List from the values: {l}")
    rl = list(reversed(l))
    print(f"Reversed list from the values: {rl}")


def sets():
    l = ["spam", "spam", "eggs", "spam", "bacon", "eggs"]
    s = set(l)
    print(f"The set of l={l} is {s}")
    # To remove duplicates we can do the following
    ls = list(set(l))
    print(f"List without duplicates: {ls}")
    # To preserve the order
    ld = list(dict.fromkeys(l).keys())
    print(f"List preserving the order: {ld}")


def needles_and_haystack():
    n_needles = 1000
    n_haystack = 10_000_000
    upper_bound = 100
    haystack = set(random.randint(0, upper_bound) for _ in range(n_haystack))
    needles = set(random.randint(0, upper_bound) for _ in range(n_needles))

    found = needles & haystack

    print(f"Found {len(found)} needles in the haystack: {found}")


def main():
    dict_comp()
    unpacking_mappings()
    merging_mappings()

    b1 = {
        "type": "book",
        "api": 2,
        "authors": ["Jim Blandy", "Jason Orendorff", "Leonora F.S. Tindall"],
    }
    b2 = {"type": "book", "api": 1, "author": "Alejandro Dumas"}

    r1 = get_creators(b1)
    r2 = get_creators(b2)
    print(f"Authors are: {r1}")
    print(f"Authors are: {r2}")

    match_extra()
    default_dicts()
    dict_views()
    sets()
    needles_and_haystack()


if __name__ == "__main__":
    main()
