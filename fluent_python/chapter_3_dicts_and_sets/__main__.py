""" Chapter 3 examples"""

from collections import defaultdict


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


if __name__ == "__main__":
    main()
