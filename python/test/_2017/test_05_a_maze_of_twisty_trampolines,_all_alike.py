import pytest

from _2017.day_05_a_maze_of_twisty_trampolines_all_alike import (parse, part1,
                                                                 part2)
from aoc.io import open_file


@pytest.fixture
def data():
    def _load(name: str):
        with open_file(2017, 5, name=name) as file:
            return parse(file.read())

    return _load


def test_examples1(data):
    input = data("example")
    assert part1(input) == 5


def test_examples2(data):
    input = data("example")
    assert part2(input) == 10


def test_input1(data):
    input = data("input")
    assert part1(input) == 356945


def test_input2(data):
    input = data("input")
    assert part2(input) == 28372145
