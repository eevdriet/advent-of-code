import pytest

from _2019.day_04_secure_container import is_valid, parse, part1, part2
from aoc.io import open_file


@pytest.fixture
def data():
    def _load(name: str):
        with open_file(2019, 4, name=name) as file:
            return parse(file.read())

    return _load


@pytest.mark.parametrize(
    "num, expected", [(111111, True), (223450, False), (123789, False)]
)
def test_examples1(num, expected):
    assert is_valid(num) == expected


def test_input1(data):
    input = data("input")
    assert part1(input) == 1246


@pytest.mark.parametrize(
    "num, expected", [(112233, True), (123444, False), (111122, True)]
)
def test_examples2(num, expected):
    assert is_valid(num, max_adj_digits=2) == expected


def test_input2(data):
    input = data("input")
    assert part2(input) == 814
