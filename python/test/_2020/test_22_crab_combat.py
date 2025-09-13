import pytest

from _2020.day_22_crab_combat import parse, part1, part2
from aoc.io import open_file


def data(name: str):
    with open_file(2020, 22, name) as file:
        return parse(file.read())


@pytest.mark.parametrize("n, expected", [(0, 306)])
def test_examples(n: int, expected: int):
    example = data(f"example{n if n else ''}")
    assert part1(example) == expected


def test_input1():
    input = data("input")
    assert part1(input) == 33561


@pytest.mark.parametrize("n, expected", [(0, 291)])
def test_examples2(n: int, expected: int):
    example = data(f"example{n if n else ''}")
    assert part2(example) == expected


def test_input2():
    input = data("input")
    assert part2(input) == ...
