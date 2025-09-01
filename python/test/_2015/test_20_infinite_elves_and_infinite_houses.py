import pytest

from _2015.day_20_infinite_elves_and_infinite_houses import parse, part1, part2
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2015, 20, FileType.INPUT) as file:
        return parse(file.read())


def test_input1(input):
    assert part1(input) == 665280


def test_input2(input):
    assert part2(input) == 705600
