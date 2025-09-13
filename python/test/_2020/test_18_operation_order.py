import pytest

from _2020.day_18_operation_order import Expression, parse, part1, part2
from aoc.io import open_file


def data(name: str):
    with open_file(2020, 18, name) as file:
        return parse(file.read())


@pytest.mark.parametrize(
    "line, expected",
    [
        ("1 + 2 * 3 + 4 * 5 + 6", 71),
        ("1 + (2 * 3) + (4 * (5 + 6))", 51),
        ("2 * 3 + (4 * 5)", 26),
        ("5 + (8 * 3 + 9 + 3 * 4 * 3)", 437),
        ("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 12240),
        ("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 13632),
    ],
)
def test_examples1(line: str, expected: int):
    expr = Expression.parse(line)
    assert expr.eval(part=1) == expected


def test_input1():
    input = data("input")
    assert part1(input) == 7147789965219


@pytest.mark.parametrize(
    "line, expected",
    [
        ("1 + 2 * 3 + 4 * 5 + 6", 231),
        ("1 + (2 * 3) + (4 * (5 + 6))", 51),
        ("2 * 3 + (4 * 5)", 46),
        ("5 + (8 * 3 + 9 + 3 * 4 * 3)", 1445),
        ("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 669060),
        ("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 23340),
    ],
)
def test_examples2(line: str, expected: int):
    expr = Expression.parse(line)
    assert expr.eval(part=2) == expected


def test_input2():
    input = data("input")
    assert part2(input) == 136824720421264
