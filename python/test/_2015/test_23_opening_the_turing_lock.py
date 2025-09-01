import pytest

from _2015.day_23_opening_the_turing_lock import parse, part1, part2
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2015, 23, FileType.INPUT) as file:
        return parse(file.read())


def test_input1(input):
    assert part1(input) == 307


def test_input2(input):
    assert part2(input) == 160
