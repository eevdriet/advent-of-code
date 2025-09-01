import pytest

from _2017.day_22_sporifica_virus import parse, part1, part2, simulate_virus
from aoc.io import open_file


@pytest.fixture
def data():
    def _load(name: str):
        with open_file(2017, 22, name=name) as file:
            return parse(file.read())

    return _load


def test_example1(data):
    example, start = data("example")

    assert simulate_virus(example, start, 7) == 5
    assert simulate_virus(example, start, 70) == 42
    assert simulate_virus(example, start, 10_000) == 5585


def test_input1(data):
    input = data("input")
    assert part1(*input) == 5182


def test_input2(data):
    input = data("input")
    assert part2(*input) == ...
