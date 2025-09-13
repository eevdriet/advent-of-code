import pytest

from _2020.day_24_lobby_layout import parse, part1, part2
from aoc.io import open_file


def data(name: str):
    with open_file(2020, 24, name) as file:
        return parse(file.read())


def test_example1():
    example = data("example")
    assert part1(example) == 10


def test_input1():
    input = data("input")
    assert part1(input) == 465


@pytest.mark.parametrize(
    "n_days, expected",
    [
        (0, 10),
        (1, 15),
        (2, 12),
        (3, 25),
        (4, 14),
        (5, 23),
        (6, 28),
        (7, 41),
        (8, 37),
        (9, 49),
        (10, 37),
        (20, 132),
        (30, 259),
        (40, 406),
        (50, 566),
        (60, 788),
        (70, 1106),
        (80, 1373),
        (90, 1844),
        (100, 2208),
    ],
)
def test_examples2(n_days: int, expected: int):
    example = data("example")
    assert part2(example, n_days) == expected


def test_input2():
    input = data("input")
    assert part2(input) == 4078
