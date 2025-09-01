import pytest
from _2016.day_25_clock_signal import parse, part1, part2
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2016, 25, FileType.INPUT) as file:
        return parse(file.read())

@pytest.fixture
def example():
    with open_file(2016, 25, FileType.EXAMPLE) as file:
        return parse(file.read())

@pytest.mark.parametrize("xyz, expected", [])
def test_examples1(xyz, expected):
    assert part1(xyz) == expected

@pytest.mark.parametrize("xyz, expected", [])
def test_examples2(xyz, expected):
    assert part2(xyz) == expected


def test_example1(example):
    assert part1(example) == ...


def test_example2(example):
    assert part2(example) == ...


@pytest.mark.skip(reason="Skip until solution found through AOC")
def test_input1(input):
    assert part1(input) == ...


@pytest.mark.skip(reason="Skip until solution found through AOC")
def test_input2(input):
    assert part2(input) == ...
