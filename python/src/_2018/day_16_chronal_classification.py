import sys

import parse as ps

from aoc.util import timed

Registers = list[int]
Op = list[int]
Sample = tuple[Registers, Op, Registers]


def assign(regs: list[int], idx: int, val: int):
    regs[idx] = val


OPS = {
    # Register
    "addr": lambda regs, a, b, c: assign(regs, c, regs[a] + regs[b]),
    "mulr": lambda regs, a, b, c: assign(regs, c, regs[a] * regs[b]),
    "banr": lambda regs, a, b, c: assign(regs, c, regs[a] & regs[b]),
    "borr": lambda regs, a, b, c: assign(regs, c, regs[a] | regs[b]),
    # Immediate
    "addi": lambda regs, a, b, c: assign(regs, c, regs[a] + b),
    "muli": lambda regs, a, b, c: assign(regs, c, regs[a] * b),
    "bani": lambda regs, a, b, c: assign(regs, c, regs[a] & b),
    "bori": lambda regs, a, b, c: assign(regs, c, regs[a] | b),
    # Other
    "setr": lambda regs, a, _, c: assign(regs, c, regs[a]),
    "seti": lambda regs, a, _, c: assign(regs, c, a),
    "gtir": lambda regs, a, b, c: assign(regs, c, int(a > regs[b])),
    "gtri": lambda regs, a, b, c: assign(regs, c, int(regs[a] > b)),
    "gtrr": lambda regs, a, b, c: assign(regs, c, int(regs[a] > regs[b])),
    "eqir": lambda regs, a, b, c: assign(regs, c, int(a == regs[b])),
    "eqri": lambda regs, a, b, c: assign(regs, c, int(regs[a] == b)),
    "eqrr": lambda regs, a, b, c: assign(regs, c, int(regs[a] == regs[b])),
}


def parse(input: str) -> tuple[list[Sample], list[Op]]:
    samples_str, ops_str = input.split("\n\n\n")

    # Collect samples
    samples: list[Sample] = []

    for block in samples_str.split("\n\n"):
        line1, line2, line3 = block.splitlines()

        before = list(ps.parse("Before: [{:d}, {:d}, {:d}, {:d}]", line1))
        operation = [int(num) for num in line2.split()]
        after = list(ps.parse("After:  [{:d}, {:d}, {:d}, {:d}]", line3))

        sample = before, operation, after
        samples.append(sample)

    # Collect operations
    ops = [[int(num) for num in line.split()] for line in ops_str.splitlines() if line]

    return samples, ops


def count_valid_ops(sample: Sample) -> int:
    count = 0
    before, op_vals, after = sample
    _, *vals = op_vals

    for op in OPS.values():
        regs = before.copy()
        op(regs, *vals)

        count += regs == after

    return count


def part1(samples: list[Sample], _ops: list[Op]) -> int:
    return sum(1 for sample in samples if count_valid_ops(sample) >= 3)


def part2(samples: list[Sample], ops: list[Op]) -> int:
    # Keep track of which codes can match which operations
    codes = {op[0] for _, op, _ in samples}
    code_names = {code: set(OPS.keys()) for code in codes}

    # Use the samples to try all possible operations and erase those not possible
    for before, op_vals, after in samples:
        code, *vals = op_vals
        possible = code_names[code].copy()

        for op_name in code_names[code]:
            regs = before.copy()

            op = OPS[op_name]
            op(regs, *vals)

            if regs != after:
                possible.discard(op_name)

        code_names[code] = possible

    # Keep assigning operations to codes that only have 1 possibility left
    code_ops = {}
    changed = True

    while changed:
        changed = False

        # Find all codes with only 1 possible operation assigned
        single_code_names = {
            code: next(iter(names))
            for code, names in code_names.items()
            if len(names) == 1 and code not in code_ops
        }

        # Assign the operation to the code and remove it from all other codes
        for code, name in single_code_names.items():
            code_ops[code] = OPS[name]

            for other_code, names in code_names.items():
                if code != other_code and name in names:
                    names.remove(name)
                    changed = True

    # Finally execute the actual operations
    regs = [0, 0, 0, 0]

    for op_vals in ops:
        code, *vals = op_vals
        op = code_ops[code]
        op(regs, *vals)

    return regs[0]


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, *parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, *parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
