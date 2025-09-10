import pytest

from _2019.day_18_many_worlds_interpretation import parse, part1, part2
from aoc.io import open_file


def data(name: str):
    with open_file(2019, 18, name) as file:
        return parse(file.read())


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 8),
        (2, 86),
        (3, 132),
        (4, 136),
        (5, 81),
    ],
)
def test_examples1(n: int, expected: int):
    example = data(f"example{n}")
    assert part1(example) == expected


def test_input1():
    input = data("input")
    assert part1(input) == 4676


@pytest.mark.parametrize(
    "n, expected",
    [
        (6, 8),
        (7, 24),
        (8, 32),
        (9, 72),
    ],
)
def test_examples2(n: int, expected: int):
    example = data(f"example{n}")
    assert part1(example) == expected


def test_input2():
    input = data("input")
    assert part2(input) == 2066
