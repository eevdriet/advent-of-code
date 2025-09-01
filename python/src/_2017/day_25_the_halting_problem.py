import sys

import parse as ps
from attrs import define

from aoc.io import open_file
from aoc.util import timed


@define
class StateRule:
    writes: tuple[int, int]
    moves: tuple[str, str]
    next_states: tuple[str, str]


@define
class Blueprint:
    start_state: str
    n_steps: int
    rules: dict[str, StateRule] = {}


"""
Begin in state A.
Perform a diagnostic checksum after 12302209 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state D.

In state C:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state C.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.

In state D:
  If the current value is 0:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state E.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.

In state E:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the right.
    - Continue with state B.

In state F:
  If the current value is 0:
    - Write the value 0.
    - Move one slot to the right.
    - Continue with state C.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the right.
    - Continue with state E.
"""


def parse(input: str) -> Blueprint:
    # Create the blueprint based on the starting state and steps
    start_lines, *state_blocks = input.split("\n\n")

    start_state, n_steps = ps.parse(
        "Begin in state {:w}.\nPerform a diagnostic checksum after {:d} steps.",
        start_lines,
    )
    blueprint = Blueprint(start_state, n_steps)

    # Add rules for all states found in subsequent lines
    for state_block in state_blocks:
        state_line, *lines = state_block.splitlines()
        assert len(lines) == 2 * 4

        state = ps.parse("In state {:w}:", state_line)[0]

        write0 = ps.search("Write the value {:d}.", lines[1])[0]
        write1 = ps.search("Write the value {:d}.", lines[5])[0]
        move0 = ps.search("Move one slot to the {:w}.", lines[2])[0]
        move1 = ps.search("Move one slot to the {:w}.", lines[6])[0]
        next0 = ps.search("Continue with state {:w}.", lines[3])[0]
        next1 = ps.search("Continue with state {:w}.", lines[7])[0]

        blueprint.rules[state] = StateRule(
            [write0, write1], [move0, move1], [next0, next1]
        )

    return blueprint


def part1(blueprint: Blueprint) -> int:
    slots = set()
    pos = 0
    state = blueprint.start_state

    for _ in range(blueprint.n_steps):
        # Determine the value on the tape and which rule to apply
        val = int(pos in slots)
        rule = blueprint.rules[state]

        match rule.writes[val]:
            case 0:
                slots.discard(pos)
            case _:
                slots.add(pos)

        pos += 1 if rule.moves[val] == "right" else -1
        state = rule.next_states[val]

    return len(slots)



def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")


if __name__ == "__main__":
    with open_file(2017, 25, "example") as file:
        part1(parse(file.read()))
