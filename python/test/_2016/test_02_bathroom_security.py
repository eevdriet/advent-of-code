import pytest

from _2016.day_02_bathroom_security import parse, part1, part2
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2016, 2, FileType.INPUT) as file:
        return parse(file.read())


@pytest.fixture
def example():
    with open_file(2016, 2, FileType.EXAMPLE) as file:
        return parse(file.read())


def test_example1(example):
    assert part1(example) == "1985"


def test_example2(example):
    assert part2(example) == "5DB3"


def test_input1(input):
    assert part1(input) == "18843"


def test_input2(input):
    assert part2(input) == "0"
