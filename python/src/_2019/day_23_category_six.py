import sys
from collections import deque

from _2019.intcode import IntCode
from aoc.util import timed


def parse(input: str) -> list[int]:
    return [int(num) for num in input.strip().split(",")]


def run_computers(memory: list[int], *, part2: bool) -> int:
    n_computers = 50
    computers = [IntCode(memory.copy()) for _ in range(n_computers)]
    computer_packets = [deque() for _ in range(n_computers)]

    nat_packet = []
    nat_packets_delivered = set()

    # Boot up computers
    for id, computer in enumerate(computers):
        outputs = computer.run([id])

    # Keep sending packets until computer 255 receives its first packet
    while True:
        if nat_packet and all(len(packets) == 0 for packets in computer_packets):
            x, y = nat_packet
            computer_packets[0].append(nat_packet)

            if part2 and (x, y) in nat_packets_delivered:
                return y

            nat_packets_delivered.add((x, y))

        for id, computer in enumerate(computers):
            packets = computer_packets[id]
            inputs = packets.popleft() if packets else [-1]

            outputs = computer.run(inputs)
            for idx in range(0, len(outputs), 3):
                address, x, y = outputs[idx : idx + 3]

                if address == 255:
                    if not part2:
                        return y

                    nat_packet = [x, y]
                    continue

                computer_packets[address].append([x, y])


def part1(memory: list[int]) -> int:
    return run_computers(memory, part2=False)


def part2(memory: list[int]) -> int:
    return run_computers(memory, part2=True)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
