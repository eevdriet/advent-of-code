import pytest

from _2017.day_12_digital_plumber import parse, part1, part2
from aoc.io import open_file


@pytest.fixture
def data():
    def _load(name: str):
        with open_file(2017, 12, name=name) as file:
            return parse(file.read())

    return _load


def test_example1(data):
    example = data("example")
    assert part1(example) == 6


def test_input1(data):
    input = data("input")
    assert part1(input) == 169


def test_example2(data):
    example = data("example")
    assert part2(example) == 2


def test_input2(data):
    input = data("input")
    assert part2(input) == 179
