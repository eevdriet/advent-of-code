import pytest

from _2017.day_15_dueling_generators import parse, part1, part2
from aoc.io import open_file


@pytest.fixture
def data():
    def _load(name: str):
        with open_file(2017, 15, name=name) as file:
            return parse(file.read())

    return _load


@pytest.mark.parametrize("starts, expected", [([65, 8921], 588)])
def test_examples1(starts, expected):
    assert part1(starts) == expected


@pytest.mark.parametrize("starts, expected", [([65, 8921], 309)])
def test_examples2(starts, expected):
    assert part2(starts) == expected


def test_input1(data):
    input = data("input")
    assert part1(input) == 567


def test_input2(data):
    input = data("input")
    assert part2(input) == 323
