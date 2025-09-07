import pytest

from _2019.day_05_sunny_with_a_chance_of_asteroids import parse, part1, part2
from aoc.io import open_file


@pytest.fixture
def data():
    def _load(name: str):
        with open_file(2019, 5, name=name) as file:
            return parse(file.read())

    return _load


@pytest.mark.parametrize("program, expected", [([3, 0, 4, 0, 99], 1)])
def test_examples(program, expected):
    assert part1(program) == expected


def test_input1(data):
    input = data("input")
    assert part1(input) == 9431221


def test_input2(data):
    input = data("input")
    assert part2(input) == 1409363
