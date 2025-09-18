import pytest

from _2023.day_04_scratchcards import parse, part1, part2
from aoc.io import open_file


def data(name: str):
    with open_file(2023, 4, name) as file:
        return parse(file.read())


@pytest.mark.parametrize("n, expected", [(0, 13)])
def test_examples1(n: int, expected: int):
    example = data(f"example{n if n else ''}")
    assert part1(example) == expected


def test_input1():
    input = data("input")
    assert part1(input) == 21213


@pytest.mark.parametrize("n, expected", [(0, 30)])
def test_examples2(n: int, expected: int):
    example = data(f"example{n if n else ''}")
    assert part2(example) == expected


def test_input2():
    input = data("input")
    assert part2(input) == 8549735
