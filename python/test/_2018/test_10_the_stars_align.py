import pytest

from _2018.day_10_the_stars_align import parse, part1, part2
from aoc.io import open_file


@pytest.fixture
def data():
    def _load(name: str):
        with open_file(2018, 10, name=name) as file:
            return parse(file.read())

    return _load


def test_example(data):
    example = data("example")

    with open_file(2018, 10, "example-word") as file:
        word = file.read()

    expected, time = part1(example)
    assert word.strip() == expected.strip()
    assert time == 3


def test_input(data):
    input = data("input")
    word = data("input-word")

    with open_file(2018, 10, "input-word") as file:
        word = file.read()

    expected, time = part1(input)
    assert word.strip() == expected.strip()
    assert time == 10681
