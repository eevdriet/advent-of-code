import heapq
import sys
from collections import defaultdict, deque

import parse as ps

from aoc.io import open_file
from aoc.util import timed

Rule = tuple[str, str]


def parse(input: str) -> list[Rule]:
    return [
        tuple(ps.parse("Step {:w} must be finished before step {:w} can begin.", line))
        for line in input.splitlines()
    ]


def complete_tasks(
    rules: list[Rule], n_elves: int = 1, base_duration: int = 0, part2: bool = False
) -> str:
    comes_before = defaultdict(list)
    comes_after = defaultdict(set)
    tasks = set()

    # Create the adjancency list of the graph
    for src, dst in rules:
        comes_before[src].append(dst)
        comes_after[dst].add(src)
        tasks |= {src, dst}

    # Keep track of tasks that are ready to be performed and that are in progress
    ready = [node for node in tasks if not comes_after[node]]
    heapq.heapify(ready)
    in_progress = []

    time = 0
    result = ""

    while ready or in_progress:
        # Assign ready tasks to idle elves
        while ready and len(in_progress) < n_elves:
            ready_task = heapq.heappop(ready)
            duration = base_duration + (1 + ord(ready_task) - ord("A"))

            heapq.heappush(in_progress, (time + duration, ready_task))

        # Go to the next completed task
        time, completed_task = heapq.heappop(in_progress)
        result += str(completed_task)

        # Try to unlock tasks that were waiting on this one
        for next_task in comes_before[completed_task]:
            comes_after[next_task].discard(completed_task)

            if not comes_after[next_task]:
                heapq.heappush(ready, next_task)

    return str(time) if part2 else result


def part1(rules: list[Rule]) -> str:
    return complete_tasks(rules, part2=False)


def part2(rules: list[Rule]) -> str:
    return complete_tasks(rules, n_elves=5, base_duration=60, part2=True)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(complete_tasks, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    with open_file(2018, 7, "example") as file:
        complete_tasks(parse(file.read()))
