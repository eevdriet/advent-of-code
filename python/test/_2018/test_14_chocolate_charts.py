import pytest

from _2018.day_14_chocolate_charts import parse, part1, part2
from aoc.io import open_file


@pytest.fixture
def data():
    def _load(name: str):
        with open_file(2018, 14, name=name) as file:
            return parse(file.read())

    return _load


@pytest.mark.parametrize(
    "n_recipes, expected",
    [(9, "5158916779"), (5, "0124515891"), (18, "9251071085"), (2018, "5941429882")],
)
def test_examples(n_recipes, expected):
    assert part1(n_recipes) == expected


def test_input1(data):
    input = data("input")
    assert part1(input) == "2107929416"


@pytest.mark.parametrize(
    "recipe_str, expected",
    [("51589", 9), ("01245", 5), ("92510", 18), ("59414", 2018)],
)
def test_examples2(recipe_str, expected):
    assert part2(recipe_str) == expected


def test_input2(data):
    input = data("input")
    assert part2(input) == "20307394"
