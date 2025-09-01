import pytest

from _2015.day_16_aunt_sue import parse, part1, part2
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2015, 16, FileType.INPUT) as file:
        return parse(file.read())


def test_input1(input):
    assert part1(input) == 373


def test_input2(input):
    assert part2(input) == 260
