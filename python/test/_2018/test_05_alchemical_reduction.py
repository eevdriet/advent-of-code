import pytest

from _2018.day_05_alchemical_reduction import (parse, part1, part2,
                                               reduce_polymer)
from aoc.io import open_file


@pytest.fixture
def data():
    def _load(name: str):
        with open_file(2018, 5, name=name) as file:
            return parse(file.read())

    return _load


@pytest.mark.parametrize("polymer, expected", [("dabAcCaCBAcCcaDA", "dabCBAcaDA")])
def test_examples(polymer, expected):
    assert reduce_polymer(polymer) == expected


@pytest.mark.parametrize("polymer, expected", [("dabAcCaCBAcCcaDA", 4)])
def test_examples2(polymer, expected):
    assert part2(polymer) == expected

def test_input1(data):
    input = data("input")
    assert part1(input) == 10878


def test_input2(data):
    input = data("input")
    assert part2(input) == 6874
