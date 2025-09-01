import pytest

from _2015.day_15_science_for_hungry_people import parse, part1, part2
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2015, 15, FileType.INPUT) as file:
        return parse(file.read())


@pytest.fixture
def example():
    with open_file(2015, 15, FileType.EXAMPLE) as file:
        return parse(file.read())


def test_example1(example):
    assert part1(example) == 62842880


def test_example2(example):
    assert part2(example) == 57600000


def test_input1(input):
    assert part1(input) == 222870


def test_input2(input):
    assert part2(input) == 117936
