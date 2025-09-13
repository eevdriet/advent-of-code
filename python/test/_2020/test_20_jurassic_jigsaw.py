import pytest

from _2020.day_20_jurassic_jigsaw import parse, part1, part2
from aoc.io import open_file


def data(name: str):
    with open_file(2020, 20, name) as file:
        return parse(file.read())


@pytest.mark.parametrize("n, expected", [(0, 20899048083289)])
def test_example1(n: int, expected: int):
    example = data(f"example{n if n else ''}")
    assert part1(example) == expected


def test_input1():
    input = data("input")
    assert part1(input) == 23386616781851


@pytest.mark.parametrize("n, expected", [(0, 273)])
def test_example2(n: int, expected: int):
    example = data(f"example{n if n else ''}")
    assert part2(example) == expected


def test_input2():
    input = data("input")
    assert part2(input) == 2376
