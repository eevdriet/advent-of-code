import pytest

from _2015.day_25_let_it_snow import parse, part1
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2015, 25, FileType.INPUT) as file:
        return parse(file.read())


@pytest.mark.parametrize(
    "row, col, expected",
    [(1, 1, 20151125), (2, 2, 21629792), (3, 3, 1601130), (4, 4, 9380097)],
)
def test_examples1(row, col, expected):
    assert part1(row, col) == expected


def test_input1(input):
    assert part1(*input) == 2650453
