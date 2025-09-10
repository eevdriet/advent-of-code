from _2019.day_24_planet_of_discord import parse, part1, part2
from aoc.io import open_file


def data(name: str):
    with open_file(2019, 24, name) as file:
        return parse(file.read())


def test_example1():
    example = data("example")
    assert part1(example) == 2129920


def test_input1():
    input = data("input")
    assert part1(input) == 26840049


def test_example2():
    example = data("example")
    assert part2(example, n_minutes=10) == 99


def test_input2():
    input = data("input")
    assert part2(input) == 1995
