import pytest

from _2016.day_18_like_a_rogue import count_safe_tiles, parse, part1, part2
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2016, 18, FileType.INPUT) as file:
        return parse(file.read())


def test_example_small():
    with open_file(2016, 18, name="example") as file:
        small = parse(file.read())

    assert count_safe_tiles(small, 1) == 3
    assert count_safe_tiles(small, 2) == 4
    assert count_safe_tiles(small, 3) == 6


def test_example_large():
    with open_file(2016, 18, name="example2") as file:
        large = parse(file.read())

    assert count_safe_tiles(large, 1) == 3
    assert count_safe_tiles(large, 2) == 8


def test_input1(input):
    assert part1(input) == 1939


def test_input2(input):
    assert part2(input) == 19999535
