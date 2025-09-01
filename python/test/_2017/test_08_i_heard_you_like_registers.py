import pytest

from _2017.day_08_i_heard_you_like_registers import parse, part1, part2
from aoc.io import open_file


@pytest.fixture
def data():
    def _load(name: str):
        with open_file(2017, 8, name=name) as file:
            return parse(file.read())

    return _load


def test_example1(data):
    example = data("example")
    assert part1(example) == 1


def test_input1(data):
    input = data("input")
    assert part1(input) == 4163


def test_example2(data):
    example = data("example")
    assert part2(example) == 10


def test_input2(data):
    input = data("input")
    assert part2(input) == 5347
