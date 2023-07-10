import typing


class City(typing.NamedTuple):
    continent: str
    name: str
    country: str


def simple_class_patterns(x):
    match x:
        case float():
            print(f"X is float and  X^2 = {x**2}")

        case dict():
            print(f"X is a dict: {x!r}")

        case int():
            print(f"X is an integer")

        case list():
            print(f"X is a list: {list!r}")

        case str():
            print(f"This is a str: {x!r}")

        case _:
            print(f"This is another type {type(x)}")


def match_asian_cities(cities: list[City]):
    results = []
    for city in cities:
        match city:
            case City(continent="Asia"):
                results.append(city)
    return results


def match_asian_countries(cities: list[City]):
    results = []
    for city in cities:
        match city:
            case City(continent="Asia", country=cc):
                results.append(cc)
    return results


def match_asian_cities_positional(cities: list[City]):
    results = []
    for city in cities:
        match city:
            case City("Asia"):
                results.append(city)
    return results


def match_asian_countries_positional(cities: list[City]):
    results = []
    for city in cities:
        match city:
            case City("Asia", _, country):
                results.append(country)
    return results
