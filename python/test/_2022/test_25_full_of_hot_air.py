import pytest

from _2022.day_25_full_of_hot_air import parse, part1
from aoc.io import open_file


def data(name: str):
    with open_file(2022, 25, name) as file:
        return parse(file.read())


@pytest.mark.parametrize("n, snafu_sum, expected", [(0, 4890, "2=-1=0")])
def test_examples1(n: int, snafu_sum: int, expected: str):
    example = data(f"example{n if n else ''}")

    assert sum(num.base10() for num in example) == snafu_sum
    assert part1(example) == expected


def test_input1():
    input = data("input")
    assert part1(input) == "2==221=-002=0-02-000"
