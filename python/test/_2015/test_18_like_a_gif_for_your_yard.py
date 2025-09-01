import pytest

from _2015.day_18_like_a_gif_for_your_yard import (game_of_life, parse, part1,
                                                   part2)
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2015, 18, FileType.INPUT) as file:
        return parse(file.read())


def test_example1():
    with open_file(2015, 18, name="example") as file:
        example = parse(file.read())

    assert game_of_life(*example, n_cycles=4) == 4


def test_example2():
    with open_file(2015, 18, name="example2") as file:
        example = parse(file.read())

    assert game_of_life(*example, n_cycles=5, corners_stay_on=True) == 17


def test_input1(input):
    assert part1(*input) == 768


def test_input2(input):
    assert part2(*input) == 781
