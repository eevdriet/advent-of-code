import pytest

from _2018.day_25_four_dimensional_adventure import parse, part1
from aoc.io import open_file


def data(name: str):
    with open_file(2018, 25, name=name) as file:
        return parse(file.read())


@pytest.mark.parametrize("n, expected", [(1, 2), (2, 4), (3, 3), (4, 8)])
def test_examples(n, expected):
    input = data(f"example{n}")
    assert part1(input) == expected


def test_input1():
    input = data("input")
    assert part1(input) == 359
