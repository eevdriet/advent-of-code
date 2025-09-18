import pytest

from _2022.day_17_pyroclastic_flow import parse, part1, part2
from aoc.io import open_file


def data(name: str):
    with open_file(2022, 17, name) as file:
        return parse(file.read())


JETS = [">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"]


@pytest.mark.parametrize("n, expected", [(0, 3068)])
def test_examples1(n: int, expected: int):
    assert part1(JETS[n]) == expected


def test_input1():
    input = data("input")
    assert part1(input) == 3090


@pytest.mark.parametrize("n, expected", [(0, 1514285714288)])
def test_examples2(n: int, expected: int):
    assert part2(JETS[n]) == expected


def test_input2():
    input = data("input")
    assert part2(input) == 1530057803453
