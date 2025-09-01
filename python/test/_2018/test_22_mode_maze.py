import pytest

from _2018.day_22_mode_maze import parse, part1, part2
from aoc.io import open_file, read_file


@pytest.fixture
def data():
    def _load(name: str):
        with open_file(2018, 22, name=name) as file:
            return parse(file.read())

    return _load


@pytest.mark.parametrize("depth, target, expected", [(510, (10, 10), 114)])
def test_examples(depth, target, expected):
    assert part1(depth, target) == expected


def test_input1(data):
    input = data("input")
    assert part1(*input) == ...


@pytest.mark.skip(reason="Skip until solution to part 1 found through AOC")
def test_input2(data):
    input = data("input")
    assert part2(input) == ...
