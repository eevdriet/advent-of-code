import pytest

from _2017.day_03_spiral_memory import parse, part1, part2
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2017, 3, FileType.INPUT) as file:
        return parse(file.read())


@pytest.mark.parametrize(
    "square, expected",
    [(1, 0), (2, 1), (8, 1), (9, 2), (10, 3), (15, 2), (25, 4), (26, 5), (1024, 31)],
)
def test_examples1(square, expected):
    assert part1(square) == expected


@pytest.mark.parametrize(
    "square, expected",
    [(3, 4), (80, 122), (329, 330)],
)
def test_examples2(square, expected):
    assert part2(square) == expected


def test_input1(input):
    assert part1(input) == 326


def test_input2(input):
    assert part2(input) == 363010
