import pytest

from _2016.day_24_air_duct_spelunking import parse, part1, part2
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2016, 24, FileType.INPUT) as file:
        return parse(file.read())


@pytest.fixture
def example():
    with open_file(2016, 24, FileType.EXAMPLE) as file:
        return parse(file.read())


def test_example1(example):
    assert part1(example) == 14


def test_input1(input):
    assert part1(input) == 470


def test_input2(input):
    assert part2(input) == 720
