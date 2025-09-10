import pytest

from _2019.day_14_space_stoichiometry import parse, part1, part2
from aoc.io import open_file


def data(name: str):
    with open_file(2019, 14, name) as file:
        return parse(file.read())


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 31),
        (2, 165),
        (3, 13312),
        (4, 180697),
        (5, 2210736),
    ],
)
def test_examples1(n: int, expected: int):
    example = data(f"example{n}")
    assert part1(example) == expected


def test_input1():
    input = data("input")
    assert part1(input) == 346961


@pytest.mark.parametrize(
    "n, expected",
    [
        (3, 82892753),
        (4, 5586022),
        (5, 460664),
    ],
)
def test_examples2(n: int, expected: int):
    example = data(f"example{n}")
    assert part2(example) == expected


def test_input2():
    input = data("input")
    assert part2(input) == 4065790
