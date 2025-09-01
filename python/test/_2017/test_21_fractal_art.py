import pytest

from _2017.day_21_fractal_art import GRID, parse, part1, part2, simulate_grid
from aoc.io import open_file


@pytest.fixture
def data():
    def _load(name: str):
        with open_file(2017, 21, name=name) as file:
            return parse(file.read())

    return _load


def test_example1(data):
    example = data("example")
    assert simulate_grid(GRID, example, 2) == 12


def test_input1(data):
    input = data("input")
    assert part1(input) == 155


def test_input2(data):
    input = data("input")
    assert part2(input) == 2449665
