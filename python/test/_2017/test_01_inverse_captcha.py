import pytest

from _2017.day_01_inverse_captcha import parse, part1, part2
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2017, 1, FileType.INPUT) as file:
        return parse(file.read())


@pytest.mark.parametrize(
    "digits, expected",
    [
        ("1122", 3),
        ("1111", 4),
        ("1234", 0),
        ("91212129", 9),
    ],
)
def test_examples1(digits, expected):
    assert part1(digits) == expected


@pytest.mark.parametrize(
    "digits, expected",
    [
        ("1212", 6),
        ("1221", 0),
        ("123425", 4),
        ("123123", 12),
        ("12131415", 4),
    ],
)
def test_examples2(digits, expected):
    assert part2(digits) == expected


def test_input1(input):
    assert part1(input) == 1253


def test_input2(input):
    assert part2(input) == 1278
