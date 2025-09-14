import sys
from enum import Enum, auto
from typing import Literal

from numpy import median

from aoc.util import timed

BRACE_PAIRS = {"(": ")", "[": "]", "{": "}", "<": ">"}


class SyntaxResult(Enum):
    CORRUPTED = auto()
    INCOMPLETE = auto()
    COMPLETE = auto()


def parse(input: str) -> list[str]:
    return [line.strip() for line in input.splitlines()]


def find_syntax_error(
    chunk: str,
) -> (
    Literal[SyntaxResult.COMPLETE]
    | tuple[Literal[SyntaxResult.CORRUPTED], str]
    | tuple[Literal[SyntaxResult.INCOMPLETE], list[str]]
):
    openings = []

    for brace in chunk:
        if brace in BRACE_PAIRS:
            openings.append(brace)
            continue

        opening = openings.pop()
        if brace != BRACE_PAIRS[opening]:
            return SyntaxResult.CORRUPTED, brace

    return (
        SyntaxResult.COMPLETE if not openings else (SyntaxResult.INCOMPLETE, openings)
    )


def part1(chunks: list[str]) -> int:
    BRACE_SCORES = {")": 3, "]": 57, "}": 1197, ">": 25137}
    score = 0

    for chunk in chunks:
        match find_syntax_error(chunk):
            case SyntaxResult.COMPLETE:
                pass
            case SyntaxResult.INCOMPLETE, *_:
                pass
            case SyntaxResult.CORRUPTED, brace:
                score += BRACE_SCORES[brace]

    return score


def part2(chunks: list[str]) -> int:
    BRACE_SCORES = {")": 1, "]": 2, "}": 3, ">": 4}
    scores = []

    for chunk in chunks:
        match find_syntax_error(chunk):
            case SyntaxResult.COMPLETE:
                pass
            case SyntaxResult.CORRUPTED, *_:
                pass
            case SyntaxResult.INCOMPLETE, openings:
                score = 0

                for opening in reversed(openings):
                    closing = BRACE_PAIRS[opening]
                    score = 5 * score + BRACE_SCORES[closing]

                scores.append(score)

    return int(median(scores))


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
