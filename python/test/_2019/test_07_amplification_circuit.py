import pytest

from _2019.day_07_amplification_circuit import parse, part1, part2
from aoc.io import open_file


def data(name: str):
    with open_file(2019, 7, name) as file:
        return parse(file.read())


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0], 43210),
        (
            [
                3,
                23,
                3,
                24,
                1002,
                24,
                10,
                24,
                1002,
                23,
                -1,
                23,
                101,
                5,
                23,
                23,
                1,
                24,
                23,
                23,
                4,
                23,
                99,
                0,
                0,
            ],
            54321,
        ),
        (
            [
                3,
                31,
                3,
                32,
                1002,
                32,
                10,
                32,
                1001,
                31,
                -2,
                31,
                1007,
                31,
                0,
                33,
                1002,
                33,
                7,
                33,
                1,
                33,
                31,
                31,
                1,
                32,
                31,
                31,
                4,
                31,
                99,
                0,
                0,
                0,
            ],
            65210,
        ),
    ],
)
def test_examples(nums, expected):
    assert part1(nums) == expected


def test_input1():
    input = data("input")
    assert part1(input) == 366376


def test_input2():
    input = data("input")
    assert part2(input) == ...
