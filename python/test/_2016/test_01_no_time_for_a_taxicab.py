import pytest

from _2016.day_01_no_time_for_a_taxicab import parse, part1, part2
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2016, 1, FileType.INPUT) as file:
        return parse(file.read())


@pytest.mark.parametrize(
    "directions, expected",
    [
        ("R2, L3", 5),
        ("R2, R2, R2", 2),
        ("R5, L5, R5, R3", 12),
    ],
)
def test_examples1(directions, expected):
    directions = parse(directions)
    assert part1(directions) == expected


@pytest.mark.parametrize(
    "directions, expected",
    [
        ("R8, R4, R4, R8", 4),
    ],
)
def test_examples2(directions, expected):
    directions = parse(directions)
    assert part2(directions) == expected


def test_input1(input):
    assert part1(input) == 246


def test_input2(input):
    assert part2(input) == 124
