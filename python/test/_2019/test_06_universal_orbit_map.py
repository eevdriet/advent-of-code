import pytest

from _2019.day_06_universal_orbit_map import parse, part1, part2
from aoc.io import read_file


def data(name: str):
    return parse(read_file(2019, 6, name))


def test_example1():
    example = data("example1")
    assert part1(example) == 42


def test_input1():
    input = data("input")
    assert part1(input) == 117672


def test_example2():
    example = data("example2")
    assert part2(example) == 4


def test_input2():
    input = data("input")
    assert part2(input) == 277
