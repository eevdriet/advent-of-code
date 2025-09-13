import pytest

from _2020.day_19_monster_messages import Monster, parse, part1, part2
from aoc.io import open_file


def data(name: str):
    with open_file(2020, 19, name) as file:
        return parse(file.read())


@pytest.mark.parametrize("n, expected", [(1, [True, False, True, False, False])])
def test_examples1(n: int, expected: list[bool]):
    rules, messages = data(f"example{n if n else ''}")
    monster = Monster(rules)

    for message, is_match in zip(messages, expected):
        assert ("" in monster.match("0", message)) == is_match


def test_input1():
    input = data("input")
    assert part1(*input) == 224


@pytest.mark.parametrize(
    "n, matching1, matching2",
    [
        (
            2,
            {"bbabbbbaabaabba", "ababaaaaaabaaab", "ababaaaaabbbaba"},
            {
                "bbabbbbaabaabba",
                "babbbbaabbbbbabbbbbbaabaaabaaa",
                "aaabbbbbbaaaabaababaabababbabaaabbababababaaa",
                "bbbbbbbaaaabbbbaaabbabaaa",
                "bbbababbbbaaaaaaaabbababaaababaabab",
                "ababaaaaaabaaab",
                "ababaaaaabbbaba",
                "baabbaaaabbaaaababbaababb",
                "abbbbabbbbaaaababbbbbbaaaababb",
                "aaaaabbaabaaaaababaa",
                "aaaabbaabbaaaaaaabbbabbbaaabbaabaaa",
                "aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba",
            },
        )
    ],
)
def test_examples12(n: int, matching1: set[str], matching2: set[str]):
    rules, messages = data(f"example{n if n else ''}")

    for message in messages:
        is_match = bool(part1(rules, [message]))
        assert is_match == (message in matching1)

        is_match = bool(part2(rules, [message]))
        assert is_match == (message in matching2)


def test_input2():
    input = data("input")
    assert part2(*input) == 436
