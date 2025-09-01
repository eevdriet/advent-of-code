from collections import deque

import pytest

from _2017.day_16_permutation_promenade import dance, parse, part1, part2
from aoc.io import open_file


@pytest.fixture
def data():
    def _load(name: str):
        with open_file(2017, 16, name=name) as file:
            return parse(file.read())

    return _load


@pytest.mark.parametrize(
    "input, expected",
    [
        ("s1", "eabcd"),
        ("x3/4", "abced"),
        ("pe/b", "aecdb"),
    ],
)
def test_examples(input, expected):
    moves = parse(input)
    program = deque(["a", "b", "c", "d", "e"])
    result = "".join(dance(program, moves))

    assert result == expected


def test_input1(data):
    input = data("input")
    assert part1(input) == "hmefajngplkidocb"


def test_input2(data):
    input = data("input")
    assert part2(input) == "fbidepghmjklcnoa"
