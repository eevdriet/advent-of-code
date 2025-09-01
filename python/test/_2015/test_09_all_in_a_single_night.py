import pytest

from _2015.day_09_all_in_a_single_night import parse, part1, part2
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2015, 9, FileType.INPUT) as file:
        return parse(file.read())


@pytest.fixture
def example():
    with open_file(2015, 9, FileType.EXAMPLE) as file:
        return parse(file.read())


def test_example1(example):
    assert part1(*example) == 605


def test_input1(input):
    assert part1(*input) == 141


def test_input2(input):
    assert part2(*input) == 736
