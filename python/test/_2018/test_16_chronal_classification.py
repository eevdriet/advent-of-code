import pytest

from _2018.day_16_chronal_classification import (count_valid_ops, parse, part1,
                                                 part2)
from aoc.io import open_file


@pytest.fixture
def data():
    def _load(name: str):
        with open_file(2018, 16, name=name) as file:
            return parse(file.read())

    return _load


def test_example1(data):
    samples, _ = data("example")
    assert count_valid_ops(samples[0]) == 3


def test_input1(data):
    input = data("input")
    assert part1(*input) == 570


def test_input2(data):
    input = data("input")
    assert part2(*input) == 503
