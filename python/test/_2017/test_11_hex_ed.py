import pytest

from _2017.day_11_hex_ed import parse, part1, part2
from aoc.io import open_file


@pytest.fixture
def data():
    def _load(name: str):
        with open_file(2017, 11, name=name) as file:
            return parse(file.read())

    return _load


@pytest.mark.parametrize(
    "directions, expected",
    [("ne,ne,ne", 3), ("ne,ne,sw,sw", 0), ("ne,ne,s,s", 2), ("se,sw,se,sw,sw", 3)],
)
def test_examples(directions, expected):
    assert part1(parse(directions)) == expected


def test_input1(data):
    input = data("input")
    assert part1(input) == 707


def test_input2(data):
    input = data("input")
    assert part2(input) == 1490
