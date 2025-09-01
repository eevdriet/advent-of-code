import pytest

from _2015.day_05_doesnt_he_have_intern_elves_for_this import (parse, part1,
                                                               part2)
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2015, 5, FileType.INPUT) as file:
        return parse(file.read())


@pytest.mark.parametrize(
    "string, expected",
    [
        ("ugknbfddgicrmopn", True),
        ("aaa", True),
        ("jchzalrnumimnmhp", False),
        ("haegwjzuvuyypxyu", False),
        ("dvszwmarrgswjxmb", False),
    ],
)
def test_examples1(string, expected):
    assert part1([string]) == int(expected)


@pytest.mark.parametrize(
    "string, expected",
    [
        ("qjhvhtzxzqqjkmpb", True),
        ("xxyxx", True),
        ("uurcxstgmygtbstg", False),
        ("ieodomkazucvgmuy", False),
    ],
)
def test_examples2(string, expected):
    assert part2([string]) == int(expected)


def test_input1(input):
    assert part1(input) == 255


def test_input2(input):
    assert part2(input) == 55
