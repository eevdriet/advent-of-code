import pytest

from _2016.day_16_dragon_checksum import (apply_checksum, apply_dragon, parse,
                                          part1, part2)
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2016, 16, FileType.INPUT) as file:
        return parse(file.read())


@pytest.mark.parametrize(
    "num, expected",
    [
        ("1", "100"),
        ("0", "001"),
        ("11111", "11111000000"),
        ("111100001010", "1111000010100101011110000"),
    ],
)
def test_dragon(num, expected):
    assert apply_dragon(num) == expected


@pytest.mark.parametrize(
    "num, expected",
    [
        ("110010110100", "110101"),
        ("110101", "100"),
    ],
)
def test_checksum(num, expected):
    assert apply_checksum(num) == expected


def test_input1(input):
    assert part1(input) == "10101001010100001"


def test_input2(input):
    assert part2(input) == "10100001110101001"
