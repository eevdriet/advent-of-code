import sys
from math import prod

from aoc.util import timed

Bus = int | None


def parse(input: str) -> tuple[int, list[Bus]]:
    first, second = input.splitlines()

    earliest_time = int(first)
    busses = [int(num) if num.isdigit() else None for num in second.split(",")]

    return earliest_time, busses


def part1(earliest_time: int, busses: list[Bus]) -> int:
    # Determine the next arrival from a given time for all busses
    # and how long you'd have to wait for them
    def next_arrival(bus: int, from_time: int) -> int:
        last_arrival = (from_time // bus) * bus
        return last_arrival + (bus if from_time % bus else 0)

    running_busses = [bus for bus in busses if isinstance(bus, int)]
    waiting_times = {
        next_arrival(bus, earliest_time) - earliest_time: bus for bus in running_busses
    }

    # Then pick the bus with the shortest wait and calculate the result
    min_waiting_time = min(waiting_time for waiting_time in waiting_times)
    min_waiting_bus = waiting_times[min_waiting_time]

    return min_waiting_time * min_waiting_bus


def part2(_: int, busses: list[Bus]) -> int:
    """
    Find for every bus the modulus and remainder to invoke the CRT
    such that we can solve the following system for x:

    x = b1 (mod n1)
    x = b2 (mod n2)
    x = b3 (mod n3)
    ...
    """
    bs = []
    ns = []

    for delay in range(len(busses)):
        if (bus := busses[delay]) is None:
            continue

        bs.append(-delay % bus)
        ns.append(bus)

    # Carry out the theorem
    N = prod(ns)
    Ns = [N // ni for ni in ns]

    xs = []
    for ni, Ni in zip(ns, Ns):
        num = Ni % ni

        x = 1
        while (x * num) % ni != 1:
            x += 1

        xs.append(x)

    return sum(bi * Ni * xi for bi, Ni, xi in zip(bs, Ns, xs)) % N


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, *parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, *parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
