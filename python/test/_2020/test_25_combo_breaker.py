from _2020.day_25_combo_breaker import parse, part1
from aoc.io import open_file


def data(name: str):
    with open_file(2020, 25, name) as file:
        return parse(file.read())


def test_input1():
    input = data("input")
    assert part1(*input) == ...
