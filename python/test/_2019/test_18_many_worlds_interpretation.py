import pytest
from _2019.day_18_many_worlds_interpretation import parse, part1, part2
from aoc.io import open_file


def data(name: str):
    with open_file(2019, 18, name) as file:
        return parse(file.read())


@pytest.mark.parametrize("xyz, expected", [])
def test_examples(xyz, expected):
    assert part1(xyz) == expected


def test_input1():
    input = data('input')
    assert part1(input) == ...


@pytest.mark.skip(reason="Skip until solution to part 1 found through AOC")
def test_input2():
    input = data('input')
    assert part2(input) == ...

