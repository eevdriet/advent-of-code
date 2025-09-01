import pytest

from _2018.day_17_reservoir_research import parse, part1, part2
from aoc.io import open_file


@pytest.fixture
def data():
    def _load(name: str):
        with open_file(2018, 17, name=name) as file:
            return parse(file.read())

    return _load


def test_example1(data):
    example = data("example")
    assert part1(example) == 57


def test_input1(data):
    input = data("input")
    assert part1(input) == 31953


def test_input2(data):
    input = data("input")
    assert part2(input) == 26410
