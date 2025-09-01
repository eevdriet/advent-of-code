import pytest

from _2017.day_18_duet import parse, part1, part2
from aoc.io import open_file


@pytest.fixture
def data():
    def _load(name: str, part2: bool):
        with open_file(2017, 18, name=name) as file:
            return parse(file.read(), part2)

    return _load


def test_example1(data):
    example = data("example", part2=False)
    assert part1(example) == 4


def test_input1(data):
    input = data("input", part2=False)
    assert part1(input) == 4601


def test_example2(data):
    example = data("example2", part2=True)
    assert part2(example) == 3


def test_input2(data):
    input = data("input", part2=True)
    assert part2(input) == ...
