import pytest

from _2016.day_03_squares_with_three_sides import Triangle, parse, part1, part2
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2016, 3, FileType.INPUT) as file:
        return parse(file.read())


@pytest.mark.parametrize("nums, expected", [([5, 10, 25], 0)])
def test_examples1(nums: list[int], expected):
    assert part1(nums) == expected


@pytest.mark.parametrize("nums, expected", [([5, 10, 25] * 3, 3)])
def test_examples2(nums, expected):
    assert part2(nums) == expected


def test_input1(input):
    assert part1(input) == 1050


def test_input2(input):
    assert part2(input) == 1921
