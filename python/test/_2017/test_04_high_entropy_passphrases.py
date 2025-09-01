import pytest

from _2017.day_04_high_entropy_passphrases import is_valid, parse, part1, part2
from aoc.io import open_file


@pytest.fixture
def data():
    def _load(name: str):
        with open_file(2017, 4, name=name) as file:
            return parse(file.read())

    return _load


@pytest.mark.parametrize(
    "phrase, expected",
    [
        ("abcde", True),
        ("abcde xyz ecdab", False),
        ("a ab abc abd abf abj", True),
        ("iiii oiii ooii oooi oooo", True),
        ("oiii ioii iioi iiio", False),
    ],
)
def test_examples2(phrase, expected):
    assert is_valid(phrase.split()) == expected


def test_input1(data):
    input = data("input")
    assert part1(input) == 477


def test_input2(data):
    input = data("input")
    assert part2(input) == 167
