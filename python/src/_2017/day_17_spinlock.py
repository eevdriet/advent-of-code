import sys

from aoc.types.list import ListNode
from aoc.util import timed


def parse(input: str) -> int:
    return int(input.strip())


def print_list(li: ListNode) -> str:
    val = li.val
    curr = li.next
    result = [str(val)]

    while curr and curr.val != val:
        result.append(str(curr.val))
        curr = curr.next

    return " -> ".join(result)


def part1(n_steps: int) -> int:
    li = ListNode(0)
    li.next = li
    li.prev = li

    curr = li

    for val in range(1, 2018):
        for _ in range(n_steps):
            curr = curr.next

        next = ListNode(val, curr, curr.next)
        curr.next = next
        curr = next

    return curr.next.val


def part2(n_steps: int) -> int:
    """
    Imagine 0 always stays in position 0
    Then we need to determine every value <= 50_000_000 that is inserted in position 0 as its ancestor
    """
    pos = 0
    candidate = -1

    for val in range(1, 50_000_000 + 1):
        pos = (pos + n_steps) % val + 1

        if pos == 1:
            candidate = val

    return candidate


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    part2(3)
