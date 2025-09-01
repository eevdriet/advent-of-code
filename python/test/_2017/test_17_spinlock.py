import pytest

from _2017.day_17_spinlock import parse, part1, part2
from aoc.io import open_file


@pytest.fixture
def data():
    def _load(name: str):
        with open_file(2017, 17, name=name) as file:
            return parse(file.read())

    return _load


@pytest.mark.parametrize("n_steps, expected", [(3, 638)])
def test_examples(n_steps, expected):
    assert part1(n_steps) == expected


def test_input1(data):
    input = data("input")
    assert part1(input) == 777


def test_input2(data):
    input = data("input")
    assert part2(input) == 39289581
