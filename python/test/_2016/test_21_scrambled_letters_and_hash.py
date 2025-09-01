import pytest

from _2016.day_21_scrambled_letters_and_hash import (parse, part1, part2,
                                                     perform)
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2016, 21, FileType.INPUT) as file:
        return parse(file.read())


@pytest.fixture
def example():
    with open_file(2016, 21, FileType.EXAMPLE) as file:
        return parse(file.read())


def test_example1(example):
    assert perform("abcde", example) == "decab"


def test_example2(example):
    assert perform("decab", example, in_reverse=True) == "abcde"


def test_input1(input):
    assert part1(input) == "gbhcefad"


@pytest.mark.skip("Cannot resolve `rotate_letter` for part 2")
def test_input2(input):
    assert part2(input) == "gahedfcb"
