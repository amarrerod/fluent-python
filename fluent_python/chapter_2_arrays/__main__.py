""" Chapter 2 examples"""

from ..chapter_1_data_model.card_deck import FrenchDeck, Card
import array
from .pattern_matching import test_robot_matching


def list_comprehension():
    symbols = "$¢£¥€¤"
    codes = []
    for symbol in symbols:
        codes.append(ord(symbol))

    # The ord() function returns an integer representing the Unicode character.
    codes_comp = [ord(symbol) for symbol in symbols]
    print(f"Codes: {codes_comp}")

    # Local scope in listcomps and genexps
    x = "ABC"
    codes = [ord(x) for x in x]
    print(f"X is: {x} and codes are: {codes}")
    # Applying walrus operator
    codes = [last := ord(c) for c in x]
    print(f"Last is: {last}")


def list_comps_vs_mapfilter():
    symbols = "$¢£¥€¤"
    beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
    print(f"Characters beyond ASCII: {beyond_ascii}")
    # Same as above but using filter and map
    beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
    print(f"Characters beyond ASCII code using list-filter-map: {beyond_ascii}")


def cartesian_shirts():
    colors = ["black", "white"]
    sizes = list("SML")
    tshirts = [(color, size) for color in colors for size in sizes]
    print(f"All T-shirts available are: {tshirts}")


def cartesian_cards():
    ranks = FrenchDeck.ranks[-3:]
    ranks.reverse()

    rank_suits_product = [(r, s) for r in ranks for s in FrenchDeck.suits]
    print(
        f"The cartersian product of R: {ranks} and S: {FrenchDeck.suits} is RxS: {rank_suits_product}"
    )


def genexps_examples():
    symbols = "$¢£¥€¤"
    codes_as_tuple = tuple(ord(symbol) for symbol in symbols)
    codes_as_array = array.array("I", (ord(symbol) for symbol in symbols))
    print(f"Codes as tuple : {codes_as_tuple}")
    print(f"Codes as array: {codes_as_array}")

    colors = ["black", "white"]
    sizes = list("SML")
    # Here the 6-item list is never built in memory
    # The generator expression feeds the for loop producing
    # one item at a time. Using genexps would save the cost of building a list just to feed the for loop
    for tshirt in (f"{c} {s}" for c in colors for s in sizes):
        print(tshirt)


def tuples_as_records():
    lax_coordinates = (33.9425, -118.408056)
    city, year, pop, chg, area = ("Tokyo", 2003, 32_450, 0.66, 8014)
    traveler_ids = [("USA", "33195855"), ("BRA", "CE342567"), ("ESP", "XDA205856")]

    for passport in sorted(traveler_ids):
        print("%s/%s" % passport)

    for country, _ in traveler_ids:
        print(country)


def tuples_as_immutable_lists():
    a = (10, "alpha", [1, 2])
    b = (10, "alpha", [1, 2])

    r = a == b
    print(f"Are A: {a} and B: {b} equal?: {r}")

    b[-1].append(99)
    r = a == b
    print(f"Are A: {a} and B: {b} equal?: {r}")


def fixed_size(o):
    """
    Checks whether a tuple only contains immutable values
    To be hashable, an object value cannot ever change
    """
    try:
        hash(o)
    except TypeError:
        return False
    return True


def unpacking_function():
    r = divmod(20, 8)
    t = (20, 8)
    r2 = divmod(*t)

    quotient, remainder = divmod(*t)
    print(f"Quotient: {quotient}, Remainder: {remainder}")


def __function_with_rest_args(a, b, c, d, *rest):
    print(f"In function.\n -A: {a}, B: {b}, C: {c}, D: {d}, Rest: {rest}")
    return a, b, c, d, rest


def grab_excess():
    a, b, *rest = range(5)
    print(f"A: {a}, B: {b}, Rest: {rest}")

    a, b, *rest = range(3)
    print(f"A: {a}, B: {b}, Rest: {rest}")

    a, b, *rest = range(2)
    print(f"A: {a}, B: {b}, Rest: {rest}")

    a, *body, c, d = range(5)
    print(f"A: {a}, Body: {body}, C: {c}, D: {d}")

    *head, b, c, d = range(5)
    print(f"Head: {head}, B: {b}, C: {c}, D: {d}")

    # A = 1
    # B = 2
    # C = 3
    # D = 4
    # Rest = (5, 6)
    result = __function_with_rest_args(*[1, 2], 3, *range(4, 7))
    print(f"Result is: {result}")

    # * can also be used when defining lists, tuples or set literals
    t = *range(4), 4
    l = [*range(4), 4]
    s = {*range(4), 4, *(5, 6, 7)}
    print(f"Tuple: {t}, List: {l}, Set: {s}")


def nested_unpacking():
    metro_areas = [
        ("Tokyo", "JP", 36.933, (35.689722, 139.691667)),
        ("Delhi NCR", "IN", 21.935, (28.613889, 77.208889)),
        ("Mexico City", "MX", 20.142, (19.433333, -99.1333333)),
        ("New York-Newark", "US", 20.104, (40.808611, -74.020386)),
        ("São Paulo", "BR", 19.649, (-23.547778, -46.635833)),
    ]

    print(f'{"City":15} | {"latitude":>9} | {"longitude":>9}')

    for name, _, _, (lat, lon) in metro_areas:
        if lon <= 0:
            print(f"{name:15} | {lat:>9.4f} | {lon:9.4f}")


def nested_destructuring():
    metro_areas = [
        ("Tokyo", "JP", 36.933, (35.689722, 139.691667)),
        ("Delhi NCR", "IN", 21.935, (28.613889, 77.208889)),
        ("Mexico City", "MX", 20.142, (19.433333, -99.1333333)),
        ("New York-Newark", "US", 20.104, (40.808611, -74.020386)),
        ("São Paulo", "BR", 19.649, (-23.547778, -46.635833)),
    ]

    print(f'{"City":15} | {"latitude":>9} | {"longitude":>9}')

    for record in metro_areas:
        match record:
            case [name, _, _, (lat, long)] if long <= 0:
                print(f"{name:15} | {lat:>9.4f} | {long:9.4f}")


def main():
    delimiter = "=" * 120
    print(delimiter)
    print(f"Running Chapter 2 examples")
    print(delimiter)

    list_comprehension()
    list_comps_vs_mapfilter()
    cartesian_shirts()
    cartesian_cards()
    genexps_examples()
    tuples_as_records()
    tuples_as_immutable_lists()
    unpacking_function()
    grab_excess()
    nested_unpacking()
    test_robot_matching()
    nested_destructuring()


if __name__ == "__main__":
    main()
