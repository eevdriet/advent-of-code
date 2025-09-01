import pytest

from _2015.day_02_i_was_told_there_would_be_no_math import (Box, parse, part1,
                                                            part2)
from aoc.io import FileType, open_file


@pytest.fixture
def input() -> list[Box]:
    with open_file(2015, 2, FileType.INPUT) as file:
        return parse(file.read())


@pytest.mark.parametrize(
    "length, width, height, expected", [(2, 3, 4, 58), (1, 1, 10, 43)]
)
def test_examples1(length: int, width: int, height: int, expected: int):
    box = Box(length, width, height)
    assert part1([box]) == expected


@pytest.mark.parametrize(
    "length, width, height, expected", [(2, 3, 4, 34), (1, 1, 10, 14)]
)
def test_example2(length: int, width: int, height: int, expected: int):
    box = Box(length, width, height)
    assert part2([box]) == expected


def test_input1(input):
    assert part1(input) == 1586300


def test_input2(input):
    assert part2(input) == 3737498
