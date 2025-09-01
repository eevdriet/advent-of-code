import pytest

from _2016.day_11_radioisotope_thermoelectric_generators import (
    find_min_steps,
    parse,
    part1,
    part2,
)
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2016, 11, FileType.INPUT) as file:
        return parse(file.read())


@pytest.fixture
def example():
    with open_file(2016, 11, FileType.EXAMPLE) as file:
        return parse(file.read())


def test_example1(example):
    assert part1(example) == 11


def test_input1(example):
    assert part1(example) == 31


def test_input2(input):
    assert part2(input) == 55
