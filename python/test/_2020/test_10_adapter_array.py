import pytest

from _2020.day_10_adapter_array import parse, part1, part2
from aoc.io import open_file


def data(name: str):
    with open_file(2020, 10, name) as file:
        return parse(file.read())


@pytest.mark.parametrize("n, expected", [(1, 35), (2, 220)])
def test_examples1(n: int, expected: int):
    example = data(f"example{n}")
    assert part1(example) == expected


def test_input1():
    input = data("input")
    assert part1(input) == 2030


@pytest.mark.parametrize("n, expected", [(1, 8), (2, 19_208)])
def test_examples12(n: int, expected: int):
    example = data(f"example{n}")
    assert part2(example) == expected


def test_input2():
    input = data("input")
    assert part2(input) == 42313823813632
