import pytest

from _2015.day_10_elves_look_elves_say import look_and_say, parse, part1, part2
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2015, 10, FileType.INPUT) as file:
        return parse(file.read())


@pytest.mark.parametrize(
    "num, expected",
    [
        ("1", "11"),
        ("11", "21"),
        ("21", "1211"),
        ("1211", "111221"),
        ("111221", "312211"),
    ],
)
def test_examples(num, expected):
    assert look_and_say(num) == expected


def test_input1(input):
    assert part1(input) == 360154


def test_input2(input):
    assert part2(input) == 5103798
