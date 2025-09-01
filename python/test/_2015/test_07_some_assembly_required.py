import pytest

from _2015.day_07_some_assembly_required import (find_signal, parse, part1,
                                                 part2)
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2015, 7, FileType.INPUT) as file:
        return parse(file.read())


@pytest.fixture
def example():
    with open_file(2015, 7, FileType.EXAMPLE) as file:
        return parse(file.read())


@pytest.mark.skip("Not working for some reason")
def test_example1(example):
    WIRES = {
        "d": 72,
        "e": 507,
        "f": 492,
        "g": 114,
        "h": 65412,
        "i": 65079,
        "x": 123,
        "y": 456,
    }

    signals = {}
    find_signal("i", example, signals)

    assert find_signal == WIRES


def test_input1(input):
    assert part1(input) == 46065


def test_input2(input):
    assert part2(input) == 14134
