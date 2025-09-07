import pytest

from _2019.day_13_care_package import parse, part1, part2
from aoc.io import open_file


def data(name: str):
    with open_file(2019, 13, name) as file:
        return parse(file.read())


def test_input1():
    input = data("input")
    assert part1(input) == 335


def test_input2():
    input = data("input")
    assert part2(input) == 15706
