import sys

from attrs import define, field

from aoc.io import read_file
from aoc.util import timed

Key = str
Terminal = str
Rule = Terminal | list[list[Key]]
Rules = dict[Key, Rule]
Message = str


@define
class Monster:
    rules: Rules
    memo: dict[tuple[Key, str], set[str]] = field(factory=dict)

    def match(self, rule_key: Key, message: str) -> set[str]:
        """Return all possible remainders after matching rule_key at start of message."""
        if (rule_key, message) in self.memo:
            return self.memo[(rule_key, message)]

        rule = self.rules[rule_key]
        remainders: set[str] = set()

        if isinstance(rule, str):  # Terminal
            if message.startswith(rule):
                remainders.add(message[len(rule) :])
        else:
            for option in rule:  # option = sequence of sub-rules
                remainders |= self.match_sequence(option, message)

        self.memo[(rule_key, message)] = remainders
        return remainders

    def match_sequence(self, sequence: list[Key], message: str) -> set[str]:
        """Match a sequence of rule keys in order against the message."""
        remainders = {message}
        for subrule in sequence:
            new_remainders = set()
            for rem in remainders:
                new_remainders |= self.match(subrule, rem)
            remainders = new_remainders
            if not remainders:
                break
        return remainders


def parse(input: str) -> tuple[Rules, list[Message]]:
    rules_text, messages_text = input.split("\n\n")

    rules: Rules = {}
    for line in rules_text.splitlines():
        rule, matches = line.split(": ")

        if matches.startswith('"') and matches.endswith('"'):
            rules[rule] = matches.strip('"')
        else:
            alts = matches.split(" | ")
            rules[rule] = [alt.split() for alt in alts]

    messages = messages_text.splitlines()
    return rules, messages


def part1(rules: Rules, messages: list[Message]) -> int:
    monster = Monster(rules)
    return sum("" in monster.match("0", msg) for msg in messages)


def part2(rules: Rules, messages: list[Message]) -> int:
    # Patch rules for recursive case
    rules2 = rules.copy()
    rules2["8"] = [["42"], ["42", "8"]]
    rules2["11"] = [["42", "31"], ["42", "11", "31"]]

    monster = Monster(rules2)
    return sum("" in monster.match("0", msg) for msg in messages)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, *parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, *parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    input = read_file(2020, 19, "example")
    print("Part 1 example:", part1(*parse(input)))
    print("Part 2 example:", part2(*parse(input)))
