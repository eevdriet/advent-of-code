import pytest

from _2016.day_10_balance_bots import assign_chips, parse, part1, part2
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2016, 10, FileType.INPUT) as file:
        return parse(file.read())


@pytest.fixture
def example():
    with open_file(2016, 10, FileType.EXAMPLE) as file:
        return parse(file.read())


def test_example1(example):
    assert assign_chips(example, end_chips=(2, 5)) == 2


def test_input1(input):
    assert part1(input) == 56


def test_input2(input):
    assert part2(input) == 7847
