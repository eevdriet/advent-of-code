import pytest

from _2020.day_03_toboggan_trajectory import parse, part1, part2
from aoc.io import open_file


def data(name: str):
    with open_file(2020, 3, name) as file:
        return parse(file.read())


@pytest.mark.parametrize("n, expected", [(1, 7)])
def test_examples(n: int, expected: int):
    example = data(f"example{n}")
    assert part1(example) == expected


def test_input1():
    input = data("input")
    assert part1(input) == 211


@pytest.mark.parametrize("n, expected", [(1, 336)])
def test_examples2(n: int, expected: int):
    example = data(f"example{n}")
    assert part2(example) == expected


def test_input2():
    input = data("input")
    assert part2(input) == 3584591857
