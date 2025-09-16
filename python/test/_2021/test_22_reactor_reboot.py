import pytest

from _2021.day_22_reactor_reboot import parse, part1, part2
from aoc.io import open_file


def data(name: str):
    with open_file(2021, 22, name) as file:
        return parse(file.read())


@pytest.mark.parametrize("n, expected", [(1, 39), (2, 590_784), (3, 474140)])
def test_examples1(n: int, expected: int):
    example = data(f"example{n if n else ''}")
    assert part1(example) == expected


def test_input1():
    input = data("input")
    assert part1(input) == 650099


@pytest.mark.parametrize("n, expected", [(3, 2758514936282235)])
def test_examples2(n: int, expected: int):
    example = data(f"example{n if n else ''}")
    assert part2(example) == expected


def test_input2():
    input = data("input")
    assert part2(input) == 1254011191104293
