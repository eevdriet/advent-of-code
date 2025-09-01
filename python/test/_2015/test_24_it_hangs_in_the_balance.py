import pytest

from _2015.day_24_it_hangs_in_the_balance import parse, part1, part2
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2015, 24, FileType.INPUT) as file:
        return parse(file.read())


@pytest.mark.parametrize("packages, expected", [([1, 2, 3, 4, 5, 7, 8, 9, 10, 11], 99)])
def test_examples1(packages, expected):
    assert part1(packages) == expected


@pytest.mark.parametrize("packages, expected", [([1, 2, 3, 4, 5, 7, 8, 9, 10, 11], 44)])
def test_examples2(packages, expected):
    assert part2(packages) == expected


def test_input1(input):
    assert part1(input) == 11846773891


def test_input2(input):
    assert part2(input) == 80393059
