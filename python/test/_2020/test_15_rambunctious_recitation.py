import pytest

from _2020.day_15_rambunctious_recitation import parse, part1, part2, speak_numbers
from aoc.io import open_file


def data(name: str):
    with open_file(2020, 15, name) as file:
        return parse(file.read())


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([0, 3, 6], 436),
        ([1, 3, 2], 1),
        ([2, 1, 3], 10),
        ([1, 2, 3], 27),
        ([2, 3, 1], 78),
        ([3, 2, 1], 438),
        ([3, 1, 2], 1836),
    ],
)
def test_examples1(nums: int, expected: int):
    assert speak_numbers(nums, 2020) == expected


def test_input1():
    input = data("input")
    assert part1(input) == 929


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([0, 3, 6], 175594),
        ([1, 3, 2], 2578),
        ([2, 1, 3], 3544142),
        ([1, 2, 3], 261214),
        ([2, 3, 1], 6895259),
        ([3, 2, 1], 18),
        ([3, 1, 2], 362),
    ],
)
def test_examples2(nums: int, expected: int):
    assert speak_numbers(nums, 30_000_000) == expected


def test_input2():
    input = data("input")
    assert part2(input) == 16671510
