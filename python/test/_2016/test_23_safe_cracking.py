import pytest

from _2016.day_23_safe_cracking import parse, part1, part2
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2016, 23, FileType.INPUT) as file:
        return parse(file.read())


@pytest.fixture
def example():
    with open_file(2016, 23, FileType.EXAMPLE) as file:
        return parse(file.read())


def test_example1(example):
    assert part1(example) == 3


def test_input1(input):
    assert part1(input) == 13050


def test_input2(input):
    assert part2(input) == ...
