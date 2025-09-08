from _2019.day_19_tractor_beam import parse, part1, part2
from aoc.io import open_file


def data(name: str):
    with open_file(2019, 19, name) as file:
        return parse(file.read())


def test_input1():
    input = data("input")
    assert part1(input) == 129


def test_input2():
    input = data("input")
    assert part2(input) == ...
