import pytest

from _2017.day_25_the_halting_problem import parse, part1
from aoc.io import open_file


@pytest.fixture
def data():
    def _load(name: str):
        with open_file(2017, 25, name=name) as file:
            return parse(file.read())

    return _load


def test_example1(data):
    example = data("example")
    assert part1(example) == 3


def test_input1(data):
    input = data("input")
    assert part1(input) == 633
