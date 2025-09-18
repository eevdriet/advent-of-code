import pytest

from _2022.day_15_beacon_exclusion_zone import parse, part1, part2
from aoc.io import open_file


def data(name: str):
    with open_file(2022, 15, name) as file:
        return parse(file.read())


@pytest.mark.parametrize("n, y, expected", [(0, 10, 26)])
def test_examples1(n: int, y: int, expected: int):
    example = data(f"example{n if n else ''}")
    assert part1(example, y) == expected


def test_input1():
    input = data("input")
    assert part1(input) == 5176944


@pytest.mark.parametrize("n, limit, expected", [(0, 20, 56000011)])
def test_examples2(n: int, limit: int, expected: int):
    example = data(f"example{n if n else ''}")
    assert part2(example, limit) == expected


def test_input2():
    input = data("input")
    assert part2(input) == 13350458933732
