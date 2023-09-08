from .member import ClubMember, HackerClubMember
from .db_handler import DBHandler
from .dublin_core import Resource, ResourceType
from .pattern_matching_classes import (
    simple_class_patterns,
    match_asian_cities,
    match_asian_countries,
    match_asian_cities_positional,
    match_asian_countries_positional,
    City,
)
from dataclasses import dataclass
from collections import namedtuple
import typing
from datetime import date


class CoordinateClassic:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


CoordinateTuple = namedtuple("Coordinate", "lat lon", defaults=[0.0, 0.0])

CoordinateTypedTuple = typing.NamedTuple("Coordinate", [("lat", float), ("lon", float)])
CoordinateTypedTuple = typing.NamedTuple("Coordinate", lat=float, lon=float)
fields_and_types = dict(lat=float, long=float)
CoordinateTypedTuple = typing.NamedTuple("Coordinate", **fields_and_types)


class CoordinateClassicTupled(typing.NamedTuple):
    lat: float = 0.0
    lon: float = 0.0
    reference: str = "WGS84"

    def __str__(self):
        ns = "N" if self.lat >= 0 else "S"
        we = "E" if self.lon >= 0 else "W"
        return f"{abs(self.lat):.1f}º{ns}, {abs(self.lon):.1f}º{we}"


@dataclass(frozen=True)
class CoordinateDataClass:
    lat: float
    lon: float

    def __str__(self):
        ns = "N" if self.lat >= 0 else "S"
        we = "E" if self.lon >= 0 else "W"
        return f"{abs(self.lat):.1f}º{ns}, {abs(self.lon):.1f}º{we}"


def city_tuple():
    City = namedtuple(
        "City",
        "name country population coordinates",
        defaults=["", "", 0, CoordinateTuple()],
    )
    tokyo = City("Tokyo", "JP", 36.933, (35.689722, 139.691667))
    print(f"Tokyo: {tokyo}")
    print(f"Population: {tokyo.population}")
    print(f"Coordinates: {tokyo.coordinates}")

    print(
        f"The fields of City are: {City._fields}, the defaults are: {City._field_defaults}"
    )

    delhi_data = ("Delta NCR", "IN", 21.935, CoordinateTuple(28.613889, 77.208889))
    delhi = City._make(delhi_data)
    print(f"Delhi is: {delhi} from data: {delhi_data} and as dict: {delhi._asdict()}")

    default_city = City()
    print(f"A default city is: {default_city}")


def member_example():
    anna = HackerClubMember("Anna Ravenscroft", handle="AnnaRaven")
    leo = HackerClubMember("Leo Rochael", handle="Leo")
    # This one raises a ValueError leo2 = HackerClubMember("Leo Rochael")
    data = dict(name="Michael", guests=[])
    michael = HackerClubMember(**data)
    print(f"{anna}")
    print(f"{michael!r}")


def init_vars():
    handler = DBHandler(10, database="My new database")
    print(handler)


def test_dublin_core():
    description = "Improving the design of existing code"
    book = Resource(
        "978-0-12-475759-9",
        "Refactoring, 2nd Edition",
        ["Martin Fowler", "Kent Beck"],
        date(2018, 11, 19),
        ResourceType.BOOK,
        description,
        "EN",
        ["computer programming", "OOP"],
    )
    print(book)


def test_patterns():
    simple_class_patterns(2.0)
    simple_class_patterns({"x": 100})
    simple_class_patterns(1)
    simple_class_patterns(["1", 2, (3, 4)])
    simple_class_patterns("x")
    simple_class_patterns(set())

    cities = [
        City("Asia", "Tokyo", "JP"),
        City("Asia", "Delhi", "IN"),
        City("North America", "Mexico City", "MX"),
        City("North America", "New York", "US"),
        City("South America", "São Paulo", "BR"),
    ]
    r = match_asian_cities(cities)
    print(f"Asian cities: {r!r}")
    r = match_asian_countries(cities)
    print(f"Asian Countries: {r!r}")

    r = match_asian_cities_positional(cities)
    print(f"Asian cities matched by position: {r!r}")

    r = match_asian_countries_positional(cities)
    print(f"Asian countries  matched by position: {r!r}")


def main():
    moscow_classic = CoordinateClassic(55.76, 37.62)
    moscow_tuple = CoordinateTuple(55.76, 37.62)
    moscow_typed_tuple = CoordinateTypedTuple(55.76, 37.62)

    location = CoordinateClassic(55.76, 37.62)
    print(
        f"Location: {location} is equal to Moscow {moscow_classic}: {location == moscow_classic}"
    )
    print(
        f"Location tuple: {moscow_tuple} is equal to CoordinateTuple: {moscow_tuple == CoordinateTuple(55.76, 37.62)}"
    )

    print(f"The type hints from typing: {typing.get_type_hints(CoordinateTypedTuple)}")

    city_tuple()
    member_example()
    test_dublin_core()
    test_patterns()


if __name__ == "__main__":
    main()
