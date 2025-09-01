import pytest

from _2015.day_13_knights_of_the_dinner_table import parse, part1, part2
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2015, 13, FileType.INPUT) as file:
        return parse(file.read())


@pytest.fixture
def example():
    with open_file(2015, 13, FileType.EXAMPLE) as file:
        return parse(file.read())


def test_example1(example):
    assert part1(*example) == 330


def test_input1(input):
    assert part1(*input) == 709


def test_input2(input):
    assert part2(*input) == 668
