import pytest

from _2020.day_07_handy_haversacks import parse, part1, part2
from aoc.io import open_file


def data(name: str):
    with open_file(2020, 7, name) as file:
        return parse(file.read())


@pytest.mark.parametrize("n, expected", [(1, 4)])
def test_examples1(n: int, expected: int):
    example = data(f"example{n}")
    assert part1(example) == expected


def test_input1():
    input = data("input")
    assert part1(input) == 257


@pytest.mark.parametrize("n, expected", [(1, 32), (2, 126)])
def test_examples2(n: int, expected: int):
    example = data(f"example{n}")
    assert part2(example) == expected


def test_input2():
    input = data("input")
    assert part2(input) == 1038
