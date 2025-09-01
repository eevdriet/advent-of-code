import pytest

from _2017.day_07_recursive_circus import parse, part1, part2
from aoc.io import open_file


@pytest.fixture
def data():
    def _load(name: str):
        with open_file(2017, 7, name=name) as file:
            return parse(file.read())

    return _load


def test_example1(data):
    example = data("example")
    assert part1(example) == "tknk"


def test_example2(data):
    example = data("example")
    assert part2(example) == 60


def test_input1(data):
    input = data("input")
    assert part1(input) == "vtzay"


def test_input2(data):
    input = data("input")
    assert part2(input) == 910
