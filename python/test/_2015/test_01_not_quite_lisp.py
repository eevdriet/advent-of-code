import pytest

from _2015.day_01_not_quite_lisp import parse, part1, part2
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2015, 1, FileType.INPUT) as file:
        return parse(file.read())


@pytest.mark.parametrize(
    "steps, expected",
    [
        ("(())", 0),
        ("(((", 3),
        ("(()(()(", 3),
        ("))(((((", 3),
        ("())", -1),
        ("))(", -1),
        (")))", -3),
        (")())())", -3),
    ],
)
def test_examples1(steps, expected):
    assert part1(steps) == expected


@pytest.mark.parametrize("steps, expected", [(")", 1), ("()())", 5)])
def test_examples2(steps, expected):
    assert part2(steps) == expected


def test_input1(input):
    assert part1(input) == 138


def test_input2(input):
    assert part2(input) == 1771
