import pytest

from _2018.day_23_experimental_emergency_teleportation import parse, part1, part2
from aoc.io import open_file


@pytest.fixture
def data():
    def _load(name: str):
        with open_file(2018, 23, name=name) as file:
            return parse(file.read())

    return _load


def test_example1(data):
    example = data("example")
    assert part1(example) == 7


def test_input1(data):
    input = data("input")
    assert part1(input) == 943


def test_example2(data):
    example = data("example2")
    assert part2(example) == 36


def test_input2(data):
    input = data("input")
    assert part2(input) == 84087816
