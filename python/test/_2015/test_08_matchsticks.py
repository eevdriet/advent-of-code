import pytest

from _2015.day_08_matchsticks import (find_n_chars_1, find_n_chars_2, parse,
                                      part1, part2)
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2015, 8, FileType.INPUT) as file:
        return parse(file.read())


@pytest.mark.parametrize(
    "code, expected",
    [('""', (2, 0)), ('"abc"', (5, 3)), (r'"aaa\"aaa"', (10, 7)), (r'"\x27"', (6, 1))],
)
def test_examples1(code, expected):
    assert find_n_chars_1(code) == expected


@pytest.mark.parametrize(
    "code, expected",
    [
        ('""', (2, 6)),
        ('"abc"', (5, 9)),
        (r'"aaa\"aaa"', (10, 16)),
        (r'"\x27"', (6, 11)),
    ],
)
def test_examples2(code, expected):
    assert find_n_chars_2(code) == expected


def test_input1(input):
    assert part1(input) == 1342


def test_input2(input):
    assert part2(input) == 2074
