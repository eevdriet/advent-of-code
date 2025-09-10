import pytest
from _{{year}}.day_{{padded_day}}_{{uslug}} import parse, part1, part2
from aoc.io import open_file


def data(name: str):
    with open_file({{year}}, {{day}}, name) as file:
        return parse(file.read())


@pytest.mark.parametrize("n, expected", [])
def test_examples(n: int, expected: int):
    example = data(f"example{n}")
    assert part1(example) == expected


def test_input1():
    input = data('input')
    assert part1(input) == ...


@pytest.mark.skip(reason="Skip until solution to part 1 found through AOC")
def test_input2():
    input = data('input')
    assert part2(input) == ...

