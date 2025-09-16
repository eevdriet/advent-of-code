import pytest

from _2022.day_12_hill_climbing_algorithm import parse, part1, part2
from aoc.io import open_file


def data(name: str):
    with open_file(2022, 12, name) as file:
        return parse(file.read())


@pytest.mark.parametrize("n, expected", [(0, 31)])
def test_examples1(n: int, expected: int):
    example = data(f"example{n if n else ''}")
    assert part1(example) == expected


def test_input1():
    input = data("input")
    assert part1(input) == 425


@pytest.mark.parametrize("n, expected", [(0, 29)])
def test_examples2(n: int, expected: int):
    example = data(f"example{n if n else ''}")
    assert part2(example) == expected


def test_input2():
    input = data("input")
    assert part2(input) == 418
