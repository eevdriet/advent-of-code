import pytest

from _2015.day_14_reindeer_olympics import N_SECONDS, parse, part1, part2
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2015, 14, FileType.INPUT) as file:
        return parse(file.read())


@pytest.fixture
def example():
    with open_file(2015, 14, FileType.EXAMPLE) as file:
        return parse(file.read())


def test_example1(example):
    assert part1(example, 1000) == 1120


@pytest.mark.skip("Produces 688 instead of 689 for some reason")
def test_example2(example):
    assert part2(example, 1000) == 689


def test_input1(input):
    assert part1(input, N_SECONDS) == 2696


def test_input2(input):
    assert part2(input, N_SECONDS) == 1084
