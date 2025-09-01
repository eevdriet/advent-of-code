import pytest

from _2018.day_18_settlers_of_the_north_pole import parse, part1, part2
from aoc.io import open_file


@pytest.fixture
def data():
    def _load(name: str):
        with open_file(2018, 18, name=name) as file:
            return parse(file.read())

    return _load


def test_example1(data):
    example = data('example')
    assert part1(example) == 1147


def test_input1(data):
    input = data('input')
    assert part1(input) == 745008

def test_input2(data):
    input = data('input')
    assert part2(input) == 219425

