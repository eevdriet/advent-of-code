import pytest

from _2018.day_24_immune_system_simulator_20xx import parse, part1, part2
from aoc.io import open_file


@pytest.fixture
def data():
    def _load(name: str):
        with open_file(2018, 24, name=name) as file:
            return parse(file.read())

    return _load


def test_example1(data):
    example = data("example")
    assert part1(*example) == 5216


def test_input1(data):
    input = data("input")
    assert part1(*input) == 15165


def test_example2(data):
    example = data("example")
    assert part2(*example) == 51


def test_input2(data):
    input = data("input")
    assert part2(*input) == 4037
