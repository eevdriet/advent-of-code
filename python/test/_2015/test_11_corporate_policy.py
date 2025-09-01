import pytest

from _2015.day_11_corporate_policy import Password, parse, part1, part2
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2015, 11, FileType.INPUT) as file:
        return parse(file.read())


@pytest.mark.parametrize(
    "repr, expected", [("abcdefgh", "abcdffaa"), ("ghijklmn", "ghjaabcc")]
)
def test_examples(repr, expected):
    password = Password(repr)

    assert str(password.next()) == expected


def test_input1(input):
    assert part1(input) == "hepxxyzz"


def test_input2(input):
    assert part2(input) == "heqaabcc"
