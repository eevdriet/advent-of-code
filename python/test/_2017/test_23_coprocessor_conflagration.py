import pytest

from _2017.day_23_coprocessor_conflagration import parse, part1, part2
from aoc.io import open_file


@pytest.fixture
def data():
    def _load(name: str):
        with open_file(2017, 23, name=name) as file:
            return parse(file.read())

    return _load


def test_input1(data):
    input = data("input")
    assert part1(input) == 3025


def test_input2(data):
    input = data("input")
    assert part2(input) == 915
