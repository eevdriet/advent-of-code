import pytest

from _2021.day_18_snailfish import Snailfish, parse, part1, part2
from aoc.io import open_file


def data(name: str):
    with open_file(2021, 18, name) as file:
        return parse(file.read())


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, "[[[[1,1],[2,2]],[3,3]],[4,4]]"),
        (2, "[[[[3,0],[5,3]],[4,4]],[5,5]]"),
        (3, "[[[[5,0],[7,4]],[5,5]],[6,6]]"),
        (4, "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]"),
        (5, "[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]"),
    ],
)
def test_addition_examples(n: int, expected: int):
    snailfishes = data(f"example{n if n else ''}")
    result = sum(snailfishes)

    assert repr(result) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("[[1,2],[[3,4],5]]", 143),
        ("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]", 1384),
        ("[[[[1,1],[2,2]],[3,3]],[4,4]]", 445),
        ("[[[[3,0],[5,3]],[4,4]],[5,5]]", 791),
        ("[[[[5,0],[7,4]],[5,5]],[6,6]]", 1137),
        ("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]", 3488),
        ("[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]", 4140),
    ],
)
def test_magnitude_examples(text: str, expected: int):
    snailfish = Snailfish.from_text(text)
    assert snailfish.magnitude == expected


def test_input1():
    input = data("input")
    assert part1(input) == 4235


@pytest.mark.parametrize(
    "n, expected",
    [
        (5, 3993),
    ],
)
def test_examples2(n: int, expected: int):
    example = data(f"example{n if n else ''}")
    assert part2(example) == expected


def test_input2():
    input = data("input")
    assert part2(input) == 4659
