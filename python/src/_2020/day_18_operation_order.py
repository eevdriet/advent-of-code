import sys

from attrs import define

from aoc.util import timed


@define
class Expression:
    tokens: list[str]

    @classmethod
    def parse(cls, expr: str) -> "Expression":
        tokens = []
        num = []

        for ch in expr:
            if ch.isdigit():
                num.append(ch)
            else:
                if num:
                    tokens.append("".join(num))
                    num = []
                if ch in "+*()":
                    tokens.append(ch)
                elif ch.isspace():
                    continue
                else:
                    raise ValueError(f"Invalid char {ch}")
        if num:
            tokens.append("".join(num))

        return cls(tokens)

    def eval(self, *, part: int) -> int:
        """
        Evaluate parsed tokens.
        part1 → left-to-right (no precedence)
        part2 → + before *
        """
        vals = []
        ops = []

        def apply_operator():
            op = ops.pop()
            right = vals.pop()
            left = vals.pop()

            val = eval(f"{left} {op} {right}")
            vals.append(val)

        def precedence(op: str) -> int:
            match part:
                case 1:
                    return 1
                case 2:
                    return 2 if op == "+" else 1
                case _:
                    raise ValueError

        for token in self.tokens:
            match token:
                # Add number to values stack
                case t if t.isdigit():
                    vals.append(int(token))

                # Add opening parens to operator stack
                case "(":
                    ops.append(token)

                # Calculate the inner result and remove the matching (
                case ")":
                    while ops and ops[-1] != "(":
                        apply_operator()
                    ops.pop()

                # Apply the remaining operators in order of precedence
                case t if t in ["+", "*"]:
                    while (
                        ops
                        and ops[-1] in "+*"
                        and precedence(ops[-1]) >= precedence(token)
                    ):
                        apply_operator()
                    ops.append(token)
                case _:
                    raise ValueError(f"Bad token {token}")

        while ops:
            apply_operator()

        return vals[-1]


def parse(input: str) -> list[Expression]:
    return [Expression.parse(line.strip()) for line in input.splitlines()]


def part1(expressions: list[Expression]) -> int:
    return sum(expression.eval(part=1) for expression in expressions)


def part2(expressions: list[Expression]) -> int:
    return sum(expression.eval(part=2) for expression in expressions)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
