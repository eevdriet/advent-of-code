import sys

from aoc.util import timed

Group = list[str]


def parse(input: str) -> list[Group]:
    return [group.splitlines() for group in input.split("\n\n")]


def part1(groups: list[Group]) -> int:
    count_sum = 0

    for group in groups:
        questions = set()

        for person_questions in group:
            questions |= {question for question in person_questions}

        count_sum += len(questions)

    return count_sum


def part2(groups: list[Group]) -> int:
    count_sum = 0

    for group in groups:
        first_person, *other_people = group
        questions = set(first_person)

        for person_questions in other_people:
            questions.intersection_update({question for question in person_questions})

        count_sum += len(questions)

    return count_sum


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
