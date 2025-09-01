import pytest

from _2015.day_19_medicine_for_rudolph import (Molecule, Replacements, parse,
                                               part1, part2)
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2015, 19, FileType.INPUT) as file:
        return parse(file.read())


@pytest.fixture
def example() -> tuple[Molecule, Replacements]:
    with open_file(2015, 19, FileType.EXAMPLE) as file:
        return parse(file.read())


def test_example1(example):
    assert part1(*example) == 4


def test_example2(example):
    _, replacements = example

    assert part2("HOH", replacements) == 3
    assert part2("HOHOHO", replacements) == 6


def test_input1(input):
    assert part1(*input) == 535


def test_input2(input):
    assert part2(*input) == 212
