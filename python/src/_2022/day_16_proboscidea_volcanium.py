import heapq
import re
import sys
from collections import defaultdict, deque

from attrs import define

from aoc.io import read_file
from aoc.util import timed


@define
class Volcano:
    valves: dict[str, int]
    edges: dict[str, set[str]]
    flows: dict[str, int]


def parse(input: str) -> Volcano:
    edges = defaultdict(set)
    valves = {}
    flows = {}

    for idx, line in enumerate(input.splitlines()):
        match = re.match(
            r"Valve (\w+) has flow rate=(.*); tunnels? leads? to valves? (.*)$", line
        )
        valve, flow, dests = match.groups()

        valves[valve] = idx
        flows[valve] = int(flow)
        edges[valve].update(dests.split(", "))

    # Filter out valves without flow
    valves = {valve: idx for idx, (valve, flow) in enumerate(flows.items()) if flow > 0}
    return Volcano(valves, edges, flows)


def compute_paths(edges: dict[str, set[str]]):
    sp = {}

    for start in edges:
        queue = deque([(start, 0)])
        seen = {start}
        distances = {}

        while queue:
            valve, dist = queue.popleft()
            distances[valve] = dist

            for nxt in edges[valve]:
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append((nxt, dist + 1))

        sp[start] = distances

    return sp


def part1(volcano: Volcano, n_minutes: int = 30) -> int:
    prio_queue = [(0, n_minutes, "AA", 0)]
    best_seen = {}  # (valve, openend valves)
    max_flow = 0

    paths = compute_paths(volcano.edges)

    while prio_queue:
        # Get the current state
        neg_flow, time_left, valve, opened = heapq.heappop(prio_queue)
        flow = -neg_flow

        # No point continuing from previous state if we cannot gain more pressure
        if (key := (valve, opened)) in best_seen and best_seen[key] >= flow:
            continue

        best_seen[key] = flow
        max_flow = max(flow, max_flow)

        for next_valve, idx in volcano.valves.items():
            # Don't go back to already openend valve
            bit = 1 << idx

            if opened & bit:
                continue

            # Determine if there's enough time to open the next valve and add the flow
            dist = paths[valve][next_valve]
            time_after_move_and_open = time_left - dist - 1

            if time_after_move_and_open <= 0:
                continue

            # Add the
            added_flow = volcano.flows[next_valve] * time_after_move_and_open

            next_state = (
                -(flow + added_flow),
                time_after_move_and_open,
                next_valve,
                opened | bit,
            )
            heapq.heappush(prio_queue, next_state)

    return max_flow


def part2(volcano: Volcano, n_minutes: int = 26) -> int:
    # Queue stores (-flow, (time_you, time_elephant), (you, elephant), opened_bitmask)
    prio_queue = [(0, (n_minutes, n_minutes), ("AA", "AA"), 0)]
    best_seen = {}  # (sorted positions, opened, time_you, time_elephant)
    max_flow = 0

    paths = compute_paths(volcano.edges)

    valves_with_flow = list(volcano.valves.items())

    while prio_queue:
        neg_flow, (time_you, time_elephant), (you, elephant), opened = heapq.heappop(
            prio_queue
        )
        flow = -neg_flow

        # Include remaining time in the key to prevent over-pruning
        key = (tuple(sorted([you, elephant])), opened, time_you, time_elephant)
        if key in best_seen and best_seen[key] >= flow:
            continue
        best_seen[key] = flow
        max_flow = max(max_flow, flow)

        # Determine unopened valves
        unopened = [v for v, idx in valves_with_flow if not (opened & (1 << idx))]
        if not unopened or (time_you <= 0 and time_elephant <= 0):
            continue

        # For each actor, possible next moves include "wait" (None) or any unopened valve
        moves_you = [None] + unopened if time_you > 0 else [None]
        moves_elephant = [None] + unopened if time_elephant > 0 else [None]

        # Generate all combinations
        for next_you in moves_you:
            for next_elephant in moves_elephant:
                # Skip if both try to open same valve
                if next_you is not None and next_you == next_elephant:
                    continue

                next_time_you, next_time_elephant = time_you, time_elephant
                added_flow = 0
                next_opened = opened

                # Handle you moving
                if next_you is not None:
                    idx_you = volcano.valves[next_you]
                    travel_you = paths[you][next_you] + 1  # move + open
                    if time_you - travel_you <= 0:
                        continue
                    next_time_you = time_you - travel_you
                    added_flow += volcano.flows[next_you] * next_time_you
                    next_opened |= 1 << idx_you
                    next_you_pos = next_you
                else:
                    next_you_pos = you

                # Handle elephant moving
                if next_elephant is not None:
                    idx_elephant = volcano.valves[next_elephant]
                    travel_elephant = paths[elephant][next_elephant] + 1
                    if time_elephant - travel_elephant <= 0:
                        continue
                    next_time_elephant = time_elephant - travel_elephant
                    added_flow += volcano.flows[next_elephant] * next_time_elephant
                    next_opened |= 1 << idx_elephant
                    next_elephant_pos = next_elephant
                else:
                    next_elephant_pos = elephant

                heapq.heappush(
                    prio_queue,
                    (
                        -(flow + added_flow),
                        (next_time_you, next_time_elephant),
                        (next_you_pos, next_elephant_pos),
                        next_opened,
                    ),
                )

    return max_flow


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    example = read_file(2022, 16, "example")
    part1(parse(example))
