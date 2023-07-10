from dataclasses import dataclass, field
from typing import ClassVar


@dataclass
class ClubMember:
    name: str
    guests: list[str] = field(default_factory=list)
    athlete: bool = field(default=False, repr=False)


@dataclass
class HackerClubMember(ClubMember):
    all_handlers: ClassVar[set[str]] = set()
    handle: str = ""

    def __post_init__(self):
        cls = self.__class__
        if self.handle == "":
            self.handle = self.name.split()[0]
        if self.handle in cls.all_handlers:
            msg = f"handle {self.handle!r} already exists."
            raise ValueError(msg)
        cls.all_handlers.add(self.handle)
