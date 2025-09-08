import pytest

from _2019.day_20_donut_maze import parse, part1, part2
from aoc.io import open_file


def data(name: str):
    with open_file(2019, 20, name) as file:
        return parse(file.read())


@pytest.mark.parametrize("n, expected", [(1, 23), (2, 58)])
def test_examples(n: int, expected: int):
    example = data(f"example{n}")
    assert part1(example) == expected


def test_input1():
    input = data("input")
    assert part1(input) == 590


def test_example1():
    example = data("example3")
    assert part2(example) == 396


def test_input2():
    input = data("input")
    assert part2(input) == ...
