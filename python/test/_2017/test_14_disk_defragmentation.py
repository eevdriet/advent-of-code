import pytest

from _2017.day_14_disk_defragmentation import parse, part1, part2
from aoc.io import open_file


@pytest.fixture
def data():
    def _load(name: str):
        with open_file(2017, 14, name=name) as file:
            return parse(file.read())

    return _load


@pytest.mark.parametrize("key_str, expected", [("flqrgnkx", 8108)])
def test_examples1(key_str, expected):
    assert part1(key_str) == expected


@pytest.mark.parametrize("key_str, expected", [("flqrgnkx", 1242)])
def test_examples2(key_str, expected):
    assert part2(key_str) == expected


def test_input1(data):
    input = data("input")
    assert part1(input) == 8222


def test_input2(data):
    input = data("input")
    assert part2(input) == 1086
