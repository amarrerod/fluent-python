from dataclasses import dataclass
from collections import namedtuple
import typing


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


if __name__ == "__main__":
    main()
