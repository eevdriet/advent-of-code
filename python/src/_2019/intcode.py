from collections import defaultdict, deque
from enum import Enum, auto


class Status(Enum):
    IDLE = auto()
    RUNNING = auto()
    HALTED = auto()
    PAUSED_AT_INPUT = auto()
    PAUSED_AT_OUTPUT = auto()


class IntCode:
    def __init__(self, memory: list[int]):
        self.mem = defaultdict(int, {idx: memory[idx] for idx in range(len(memory))})
        self.rel_base = 0
        self.ip = 0
        self.status = Status.IDLE

    def _get(self, src: int, mode: int) -> int:
        match mode:
            case 0:
                return self.mem[src]
            case 1:
                return src
            case 2:
                return self.mem[src + self.rel_base]

        raise ValueError(f"bad mode {mode}")

    def _get_addr(self, param: int, mode: int) -> int:
        """Resolve write-address depending on mode"""
        match mode:
            case 0:
                return param
            case 2:
                return param + self.rel_base
            case _:
                raise ValueError(f"invalid mode {mode} for write parameter")

    def run(
        self, inputs: list[int] | None = None, *, pause_at_output: bool = False
    ) -> list[int]:
        inputs = inputs if inputs else []

        if self.status == Status.IDLE:
            self.status = Status.RUNNING

        inp: deque[int] = deque(inputs)
        outputs = []

        while True:
            instr = self.mem[self.ip]
            op = instr % 100
            mode1 = (instr // 100) % 10
            mode2 = (instr // 1000) % 10
            mode3 = (instr // 10000) % 10

            match op:
                case 1:  # add
                    a, b, dst = (
                        self.mem[self.ip + 1],
                        self.mem[self.ip + 2],
                        self.mem[self.ip + 3],
                    )
                    self.mem[self._get_addr(dst, mode3)] = self._get(
                        a, mode1
                    ) + self._get(b, mode2)
                    self.ip += 4

                case 2:  # multiply
                    a, b, dst = (
                        self.mem[self.ip + 1],
                        self.mem[self.ip + 2],
                        self.mem[self.ip + 3],
                    )
                    self.mem[self._get_addr(dst, mode3)] = self._get(
                        a, mode1
                    ) * self._get(b, mode2)
                    self.ip += 4

                case 3:  # input
                    dst = self.mem[self.ip + 1]

                    if not inp:
                        self.status = Status.PAUSED_AT_INPUT
                        break

                    self.mem[self._get_addr(dst, mode1)] = inp.popleft()
                    self.ip += 2

                case 4:  # output
                    src = self.mem[self.ip + 1]
                    self.ip += 2

                    out = self._get(src, mode1)
                    outputs.append(out)

                    if pause_at_output:
                        self.status = Status.PAUSED_AT_OUTPUT
                        break

                case 5:  # jump-if-true
                    a, b = self.mem[self.ip + 1], self.mem[self.ip + 2]
                    self.ip = (
                        self._get(b, mode2) if self._get(a, mode1) != 0 else self.ip + 3
                    )

                case 6:  # jump-if-false
                    a, b = self.mem[self.ip + 1], self.mem[self.ip + 2]
                    self.ip = (
                        self._get(b, mode2) if self._get(a, mode1) == 0 else self.ip + 3
                    )

                case 7:  # less than
                    a, b, dst = (
                        self.mem[self.ip + 1],
                        self.mem[self.ip + 2],
                        self.mem[self.ip + 3],
                    )
                    self.mem[self._get_addr(dst, mode3)] = (
                        1 if self._get(a, mode1) < self._get(b, mode2) else 0
                    )
                    self.ip += 4

                case 8:  # equals
                    a, b, dst = (
                        self.mem[self.ip + 1],
                        self.mem[self.ip + 2],
                        self.mem[self.ip + 3],
                    )
                    self.mem[self._get_addr(dst, mode3)] = (
                        1 if self._get(a, mode1) == self._get(b, mode2) else 0
                    )
                    self.ip += 4

                case 9:  # adjust relative base
                    param = self.mem[self.ip + 1]
                    self.rel_base += self._get(param, mode1)
                    self.ip += 2

                case 99:
                    self.status = Status.HALTED
                    break

                case _:
                    raise RuntimeError(f"Unknown opcode {op} at ip={self.ip}")

        return outputs
