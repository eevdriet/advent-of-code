from _2019.day_25_cryostasis import parse, part1_auto
from aoc.io import open_file


def data(name: str):
    with open_file(2019, 25, name) as file:
        return parse(file.read())


def test_input():
    input = data("input")
    assert part1_auto(input) == 262848
