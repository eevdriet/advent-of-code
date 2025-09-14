import pytest

from _2021.day_14_extended_polymerization import parse, part1, part2
from aoc.io import open_file


def data(name: str):
    with open_file(2021, 14, name) as file:
        return parse(file.read())


@pytest.mark.parametrize("n, expected", [(0, 1588)])
def test_examples1(n: int, expected: int):
    example = data(f"example{n if n else ''}")
    assert part1(example) == expected


def test_input1():
    input = data("input")
    assert part1(input) == 3048


@pytest.mark.parametrize("n, expected", [(0, 2188189693529)])
def test_examples2(n: int, expected: int):
    example = data(f"example{n if n else ''}")
    assert part2(example) == expected


def test_input2():
    input = data("input")
    assert part2(input) == 3288891573057
