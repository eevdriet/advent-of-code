import pytest

from _2015.day_17_no_such_thing_as_too_much import parse, part1, part2
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2015, 17, FileType.INPUT) as file:
        return parse(file.read())


@pytest.fixture
def example():
    with open_file(2015, 17, FileType.EXAMPLE) as file:
        return parse(file.read())


def test_example1(example):
    assert part1(example, 25) == 4


def test_example2(example):
    assert part2(example, 25) == 3


def test_input1(input):
    assert part1(input) == 1304


def test_input2(input):
    assert part2(input) == 18
