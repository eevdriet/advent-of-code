import pytest

from _2015.day_04_the_ideal_stocking_stuffer import parse, part1, part2
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2015, 4, FileType.INPUT) as file:
        return parse(file.read())


@pytest.mark.parametrize("key, expected", [("abcdef", 609043), ("pqrstuv", 1048970)])
def test_examples1(key, expected):
    assert part1(key) == expected


def test_input1(input):
    assert part1(input) == 117946


def test_input2(input):
    assert part2(input) == 3938038
