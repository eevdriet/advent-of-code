import pytest

from _2019.day_02_1202_program_alarm import parse, part1, part2, run
from aoc.io import open_file


@pytest.fixture
def data():
    def _load(name: str):
        with open_file(2019, 2, name=name) as file:
            return parse(file.read())

    return _load


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50], 3500),
        ([1, 0, 0, 0, 99], 2),
        ([2, 4, 4, 5, 99, 0], 2),
        ([1, 1, 1, 4, 99, 5, 6, 0, 99], 30),
    ],
)
def test_examples(nums, expected):
    assert run(nums) == expected


def test_input1(data):
    input = data("input")
    assert part1(input) == 2782414


def test_input2(data):
    input = data("input")
    assert part2(input) == 9820
