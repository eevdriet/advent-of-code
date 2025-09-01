import pytest

from _2015.day_21_rpg_simulator_20xx import parse_player, part1, part2
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2015, 21, FileType.INPUT) as file:
        return parse_player(file.read())


def test_input1(input):
    assert part1(input) == 111


def test_input2(input):
    assert part2(input) == 188
