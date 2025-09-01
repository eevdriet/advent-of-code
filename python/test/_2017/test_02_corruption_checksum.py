import pytest

from _2017.day_02_corruption_checksum import parse, part1, part2
from aoc.io import FileType, open_file


@pytest.fixture
def data():
    def _load(name: str):
        with open_file(2017, 2, name=name) as file:
            return parse(file.read())

    return _load


@pytest.fixture
def example():
    with open_file(2017, 2, FileType.EXAMPLE) as file:
        return parse(file.read())


def test_example1(data):
    example = data("example")
    assert part1(example) == 18


def test_example2(data):
    example = data("example2")
    assert part2(example) == 9


def test_input1(data):
    input = data("input")
    assert part1(input) == 39126


def test_input2(data):
    input = data("input")
    assert part2(input) == 258
