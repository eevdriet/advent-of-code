import pytest

from _2016.day_14_one_time_pad import parse, part1, part2
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2016, 14, FileType.INPUT) as file:
        return parse(file.read())


@pytest.mark.parametrize("salt, expected", [("abc", 22728)])
def test_examples1(salt, expected):
    assert part1(salt) == expected


@pytest.mark.parametrize("salt, expected", [("abc", 22551)])
def test_examples2(salt, expected):
    assert part2(salt) == expected


def test_input1(input):
    assert part1(input) == 16106


def test_input2(input):
    assert part2(input) == 22423
