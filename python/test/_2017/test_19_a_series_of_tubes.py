import pytest

from _2017.day_19_a_series_of_tubes import parse, part1, part2
from aoc.io import open_file


@pytest.fixture
def data():
    def _load(name: str):
        with open_file(2017, 19, name=name) as file:
            return parse(file.read())

    return _load


def test_example1(data):
    example = data("example")
    assert part1(*example) == "ABCDEF"


def test_input1(data):
    input = data("input")
    assert part1(*input) == "DWNBGECOMY"


def test_example2(data):
    example = data("example")
    assert part2(*example) == 38


def test_input2(data):
    input = data("input")
    assert part2(*input) == 17228
