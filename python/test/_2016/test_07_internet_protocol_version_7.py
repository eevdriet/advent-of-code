import pytest

from _2016.day_07_internet_protocol_version_7 import (Address, parse, part1,
                                                      part2)
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2016, 7, FileType.INPUT) as file:
        return parse(file.read())


@pytest.mark.parametrize(
    "text, expected",
    [
        ("abba[mnop]qrst", True),
        ("abcd[bddb]xyyx", False),
        ("aaaa[qwer]tyui", False),
        ("ioxxoj[asdfgh]zxcvbn", True),
    ],
)
def test_examples1(text, expected):
    address = Address.parse(text)
    assert address.supports_ip() == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("aba[bab]xyz", True),
        ("xyx[xyx]xyx", False),
        ("aaa[kek]eke", True),
        ("zazbz[bzb]cdb", True),
    ],
)
def test_examples2(text, expected):
    address = Address.parse(text)
    assert address.supports_ssl() == expected


def test_input1(input):
    assert part1(input) == 110


def test_input2(input):
    assert part2(input) == 0
