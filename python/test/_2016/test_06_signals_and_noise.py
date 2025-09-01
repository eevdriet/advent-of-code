import pytest

from _2016.day_06_signals_and_noise import parse, part1, part2
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2016, 6, FileType.INPUT) as file:
        return parse(file.read())


@pytest.fixture
def example():
    with open_file(2016, 6, FileType.EXAMPLE) as file:
        return parse(file.read())


def test_example1(example):
    assert part1(example) == "easter"


def test_example2(example):
    assert part2(example) == "advent"


def test_input1(input):
    assert part1(input) == "umejzgdw"


def test_input2(input):
    assert part2(input) == "aovueakv"
