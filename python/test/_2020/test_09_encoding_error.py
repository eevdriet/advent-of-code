import pytest

from _2020.day_09_encoding_error import parse, part1, part2
from aoc.io import open_file


def data(name: str):
    with open_file(2020, 9, name) as file:
        return parse(file.read())


@pytest.mark.parametrize("n, preamble, expected", [(1, 25, 48), (2, 5, 127)])
def test_examples1(n: int, preamble: int, expected: int):
    example = data(f"example{n}")
    assert part1(example, preamble=preamble) == expected


def test_input1():
    input = data("input")
    assert part1(input) == 90433990


@pytest.mark.parametrize("n, preamble, expected", [(2, 5, 62)])
def test_examples2(n: int, preamble: int, expected: int):
    example = data(f"example{n}")
    assert part2(example, preamble=preamble) == expected


def test_input2():
    input = data("input")
    assert part2(input) == 11691646
