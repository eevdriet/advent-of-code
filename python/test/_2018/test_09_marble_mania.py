import pytest

from _2018.day_09_marble_mania import parse, part1, part2
from aoc.io import open_file


@pytest.fixture
def data():
    def _load(name: str):
        with open_file(2018, 9, name=name) as file:
            return parse(file.read())

    return _load


@pytest.mark.parametrize(
    "n_players, last_marble, expected",
    [
        (10, 1618, 8317),
        (13, 7999, 146373),
        (17, 1104, 2764),
        (21, 6111, 54718),
        (30, 5807, 37305),
    ],
)
def test_examples(n_players, last_marble, expected):
    assert part1(n_players, last_marble) == expected


def test_input1(data):
    input = data("input")
    assert part1(*input) == 423717


def test_input2(data):
    input = data("input")
    assert part2(*input) == 3553108197
