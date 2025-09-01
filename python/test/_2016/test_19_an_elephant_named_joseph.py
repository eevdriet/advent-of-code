import pytest

from _2016.day_19_an_elephant_named_joseph import parse, part1, part2
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2016, 19, FileType.INPUT) as file:
        return parse(file.read())


@pytest.mark.parametrize(
    "n_elves, expected",
    [
        (5, 3),
    ],
)
def test_examples1(n_elves, expected):
    assert part1(n_elves) == expected


@pytest.mark.parametrize(
    "n_elves, expected",
    [
        (5, 2),
    ],
)
def test_examples2(n_elves, expected):
    assert part2(n_elves) == expected


def test_input1(input):
    assert part1(input) == 1841611


def test_input2(input):
    assert part2(input) == 1423634
