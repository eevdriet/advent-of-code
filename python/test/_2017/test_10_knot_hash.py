import pytest

from _2017.day_10_knot_hash import parse, part1, part2, tie_knots
from aoc.io import open_file


@pytest.fixture
def data():
    def _load(name: str):
        with open_file(2017, 10, name=name) as file:
            return parse(file.read())

    return _load


@pytest.mark.parametrize("lengths, size, expected", [([3, 4, 1, 5], 5, 12)])
def test_example1(lengths, size, expected):
    assert tie_knots(lengths, size) == str(expected)


@pytest.mark.parametrize(
    "input, expected",
    [
        ("", "a2582a3a0e66e6e86e3812dcb672a272"),
        ("AoC 2017", "33efeb34ea91902bb2f59c9920caa6cd"),
        ("1,2,3", "3efbe78a8d82f29979031a4aa0b16a9d"),
        ("1,2,4", "63960835bcdc130f0b66d7ff4f6a5a8e"),
    ],
)
def test_example2(input, expected):
    assert part2(input) == str(expected)


def test_input1(data):
    input = data("input")
    assert part1(input) == "15990"


def test_input2(data):
    input = data("input")
    result = part2(input)
    assert len(result) == 32
    assert result == "90adb097dd55dea8305c900372258ac6"
