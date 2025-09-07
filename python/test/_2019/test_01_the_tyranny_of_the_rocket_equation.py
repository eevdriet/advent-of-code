import pytest

from _2019.day_01_the_tyranny_of_the_rocket_equation import parse, part1, part2
from aoc.io import open_file


@pytest.fixture
def data():
    def _load(name: str):
        with open_file(2019, 1, name=name) as file:
            return parse(file.read())

    return _load


@pytest.mark.parametrize(
    "num, expected", [(12, 2), (14, 2), (1969, 654), (100756, 33583)]
)
def test_examples1(num, expected):
    assert part1([num]) == expected


def test_input1(data):
    input = data("input")
    assert part1(input) == 3297896


@pytest.mark.parametrize(
    "num, expected",
    [
        (14, 2),
        (1969, 654 + 216 + 70 + 21 + 5),
        (100756, 33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2),
    ],
)
def test_examples2(num, expected):
    assert part2([num]) == expected


def test_input2(data):
    input = data("input")
    assert part2(input) == 4943969
