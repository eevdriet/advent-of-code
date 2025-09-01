import pytest

from _2015.day_03_perfectly_spherical_houses_in_a_vacuum import (parse, part1,
                                                                 part2)
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2015, 3, FileType.INPUT) as file:
        return parse(file.read())


@pytest.mark.parametrize("moves, expected", [(">", 2), ("^>v<", 4), ("^v^v^v^v^v", 2)])
def test_examples1(moves, expected):
    assert part1(moves) == expected


@pytest.mark.parametrize(
    "moves, expected", [("^v", 3), ("^>v<", 3), ("^v^v^v^v^v", 11)]
)
def test_examples2(moves, expected):
    assert part2(moves) == expected


def test_input1(input):
    assert part1(input) == 2572


def test_input2(input):
    assert part2(input) == 2631
