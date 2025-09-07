import pytest

from _2019.day_12_the_n_body_problem import parse, part1, part2, simulate
from aoc.io import open_file


def data(name: str):
    with open_file(2019, 12, name) as file:
        return parse(file.read())


@pytest.mark.parametrize("n, n_steps, expected", [(1, 10, 179), (2, 100, 1940)])
def test_examples1(n, n_steps, expected):
    example = data(f"example{n}")
    simulate(example, n_steps)

    assert sum(moon.energy for moon in example) == expected


def test_input1():
    input = data("input")
    assert part1(input) == 7687


def test_input2():
    input = data("input")
    assert part2(input) == 334945516288044
