import pytest

from _2021.day_17_trick_shot import parse, part1, part2
from aoc.io import open_file


def data(name: str):
    with open_file(2021, 17, name) as file:
        return parse(file.read())


@pytest.mark.parametrize("text, expected", [("target area: x=20..30, y=-10..-5", 45)])
def test_examples1(text: str, expected: int):
    example = parse(text)
    assert part1(example) == expected


def test_input1():
    input = data("input")
    assert part1(input) == 11781


@pytest.mark.parametrize("text, expected", [("target area: x=20..30, y=-10..-5", 112)])
def test_examples2(text: str, expected: int):
    example = parse(text)
    assert part2(example) == expected


def test_input2():
    input = data("input")
    assert part2(input) == 4531
