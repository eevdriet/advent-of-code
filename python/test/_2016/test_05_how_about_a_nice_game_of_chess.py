import pytest

from _2016.day_05_how_about_a_nice_game_of_chess import parse, part1, part2
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2016, 5, FileType.INPUT) as file:
        return parse(file.read())


@pytest.mark.parametrize(
    "door_id, expected",
    [
        ("abc", "18f47a30"),
    ],
)
def test_examples1(door_id, expected):
    assert part1(door_id) == expected


@pytest.mark.skip()
def test_examples2(door_id, expected):
    assert part2(door_id) == expected


def test_input1(input):
    assert part1(input) == "1a3099aa"


def test_input2(input):
    assert part2(input) == "694190cd"
