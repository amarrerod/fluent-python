from .bingo import BingoCage
from functools import reduce, partial
from operator import mul, itemgetter, attrgetter, methodcaller
from collections import namedtuple


def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n - 1)


def factorial_reduce(n):
    return reduce(lambda a, b: a * b, range(1, n + 1))


def factorial_mult(n):
    return reduce(mul, range(1, n + 1))


def first_class_example():
    fact = factorial
    print(f"Fact is a function:  {fact}")
    print(f"Calling factorial through fact: {fact(5)}")
    # Passing the function as an argument
    print(f"Passing factorial as an argument for map {map(factorial, range(11))}")
    r = list(map(factorial, range(11)))
    print(f"The result of map is: {r}")


# From positional to keyword-only parameters
def tag(name, *content, class_=None, **attrs):
    """Generate one or more HTML tags"""
    if class_ is not None:
        attrs["class"] = class_

    attr_pairs = (f' {attr} = "{value}"' for attr, value in sorted(attrs.items()))
    attr_str = "".join(attr_pairs)
    if content:
        elements = (f"<{name}{attr_str}>{c}</{name}>" for c in content)

        return "\n".join(elements)
    else:
        return f"<{name}{attr_str}/>"


def ittem_getter_example():
    metro_areas = [
        ("Tokyo", "JP", 36.933, (35.689722, 139.691667)),
        ("Delhi NCR", "IN", 21.935, (28.613889, 77.208889)),
        ("Mexico City", "MX", 20.142, (19.433333, -99.1333333)),
        ("New York-Newark", "US", 20.104, (40.808611, -74.020386)),
        ("São Paulo", "BR", 19.649, (-23.547778, -46.635833)),
    ]
    # Sorting a list of tuples by the second value using itemgetter(1)
    for city, *other, (lat, lon) in sorted(metro_areas, key=itemgetter(1)):
        print(f"The city is: {city} at long={lat},lat={lon}")

    # Passing multiple index creates a function which return tuples with the extracted values
    c_loc = itemgetter(1, 0, 3)
    for city in metro_areas:
        print(c_loc(city))


def attr_getter_example():
    LatLon = namedtuple("LatLon", "lat lon")
    Metropolis = namedtuple("Metropolis", "name cc, pop coord")

    metro_data = [
        ("Tokyo", "JP", 36.933, (35.689722, 139.691667)),
        ("Delhi NCR", "IN", 21.935, (28.613889, 77.208889)),
        ("Mexico City", "MX", 20.142, (19.433333, -99.1333333)),
        ("New York-Newark", "US", 20.104, (40.808611, -74.020386)),
        ("São Paulo", "BR", 19.649, (-23.547778, -46.635833)),
    ]

    metro_areas = [
        Metropolis(name, cc, pop, LatLon(lat, lon))
        for name, cc, pop, (lat, lon) in metro_data
    ]

    print(f"First metro area is: {metro_areas[0]}")
    print(f"Latitude of the first metro area is: {metro_areas[0].coord.lat}")

    # Now using attrgetter
    name_lat = attrgetter(
        "name", "coord.lat"
    )  # We use attrgetter to retrieve the name and the coord.lat of the city
    for city in sorted(
        metro_areas, key=attrgetter("coord.lat")
    ):  # We sort the list by the coord.lat attribute
        print(name_lat(city))


def partial_example():
    triple_fn = partial(mul, 3)
    print(f"The triple of 7 is {triple_fn(7)}")
    l = list(range(1, 10))
    r = list(map(triple_fn, l))  # Here map
    print(f"The triple of the items {l} are {r}")


def main():
    print(f"42! = {factorial(42)}")
    print(f"The documentation of factorial(n) is: {factorial.__doc__}")
    print(f"The type of factorial is: {type(factorial)}")

    first_class_example()

    fruits = ["strawberry", "fig", "apple", "cherry", "raspberry", "banana"]
    sorted_fruits = sorted(fruits, key=lambda word: word[::-1])
    print(f"Original list: {fruits} vs Sorted list: {sorted_fruits}")

    bingo = BingoCage(range(10))
    print(f"Bingo picks: {bingo()}")
    print(f"Another pick is: {bingo()}")
    print(f"Is BingoCage callable?: {callable(bingo)}")

    print(tag("br"))
    print(tag("p", "hello"))
    print(tag("p", "hello", "world"))
    print(tag("p", "hello", id=33))
    print(tag("p", "hello", "world", class_="sidebar"))
    print(tag(content="testing", name="img"))
    my_tag = {
        "name": "img",
        "title": "Sunset Boulevard",
        "src": "sunset.jpg",
        "class": "framed",
    }
    print(tag(**my_tag))

    ittem_getter_example()
    attr_getter_example()

    s = "THE TIME HAS COME"

    hyphenate = methodcaller("replace", " ", "-")
    lowercase = methodcaller("lower")
    capitalcase = methodcaller("capitalize")
    print(hyphenate(s))
    print(capitalcase(lowercase(hyphenate(s))))

    partial_example()


if __name__ == "__main__":
    main()
