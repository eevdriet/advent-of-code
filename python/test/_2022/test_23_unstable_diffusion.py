import pytest

from _2022.day_23_unstable_diffusion import parse, part1, part2
from aoc.io import open_file


def data(name: str):
    with open_file(2022, 23, name) as file:
        return parse(file.read())


@pytest.mark.parametrize("n, expected", [(1, 110), (2, 25)])
def test_examples1(n: int, expected: int):
    example = data(f"example{n if n else ''}")
    assert part1(example) == expected


def test_input1():
    input = data("input")
    assert part1(input) == 3920


@pytest.mark.parametrize("n, expected", [(1, 20), (2, 4)])
def test_examples2(n: int, expected: int):
    example = data(f"example{n if n else ''}")
    assert part2(example) == expected


def test_input2():
    input = data("input")
    assert part2(input) == 889
