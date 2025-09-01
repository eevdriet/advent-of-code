import pytest

from _2016.day_13_a_maze_of_twisty_little_cubicles import (find_goal, parse,
                                                           part1, part2)
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2016, 13, FileType.INPUT) as file:
        return parse(file.read())


@pytest.mark.parametrize("goal, key, expected", [((7, 4), 10, 11)])
def test_examples1(goal, key, expected):
    assert find_goal(goal, key) == expected


def test_input1(input):
    assert part1(input) == 96


def test_input2(input):
    assert part2(input) == 141
