from contextlib import contextmanager
from enum import StrEnum
from pathlib import Path
from typing import Any, Generator, Optional, TextIO

DATA_PATH = Path(__file__).parent.parent.parent.parent / "data"


class FileType(StrEnum):
    INPUT = "input"
    EXAMPLE = "example"


@contextmanager
def open_file(year: int, day: int, name: str = "input") -> Generator[TextIO, Any, Any]:
    path = DATA_PATH / str(year) / f"{day:02}.{name}"

    file = open(path, mode="r", encoding="utf-8")
    try:
        yield file
    finally:
        file.close()


def read_file(year: int, day: int, name: str = "input") -> str:
    with open_file(year, day, name) as file:
        return file.read()
