import pytest

from _2017.day_06_memory_reallocation import parse, part1, part2
from aoc.io import open_file


@pytest.fixture
def data():
    def _load(name: str):
        with open_file(2017, 6, name=name) as file:
            return parse(file.read())

    return _load


@pytest.mark.parametrize("memory, expected", [([0, 2, 7, 0], 5)])
def test_examples1(memory, expected):
    assert part1(memory) == expected


@pytest.mark.parametrize("memory, expected", [([2, 4, 1, 2], 4)])
def test_examples2(memory, expected):
    assert part2(memory) == expected


def test_input1(data):
    input = data("input")
    assert part1(input) == 14029


def test_input2(data):
    input = data("input")
    assert part2(input) == 2765
