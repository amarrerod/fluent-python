from dataclasses import dataclass, InitVar
from typing import NewType


DatabaseType = NewType("DatabaseType", str)


@dataclass
class DBHandler:
    i: int
    j: int
    database: InitVar[DatabaseType] = None

    def __post_init__(self, database):
        if self.j is None and database is not None:
            self.j = database.len()
