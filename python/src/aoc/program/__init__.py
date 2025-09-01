from abc import ABC
from collections import defaultdict
from typing import Generic, Mapping, Optional, TypeVar

P = TypeVar("P", bound="Program")
O = TypeVar("O", bound="Operation")


class Operation(ABC, Generic[P]):
    def execute(self, program: P):
        pass

    def advance(self, program: P):
        program += 1


class Program[T]:
    def __init__(self, name: str, registries: Optional[Mapping[T, int]] = None):
        self.name = name
        self.ip = 0
        self.halted = False

        # Set up registers
        self.registers = defaultdict(int)
        if registries:
            for reg, val in registries.items():
                self.registers[reg] = val

        self.operations = []

    def run(self, operations: list[Operation]):
        self.operations = operations
        self.ip = 0

        while self._should_continue() and not self.halted:
            operation = self.operations[self.ip]
            self._execute(operation)

        self.halted = True

    def halt(self):
        self.halted = True

    def is_halted(self) -> bool:
        return self.halted

    def _execute(self, operation: Operation):
        operation.execute(self)
        operation.advance(self)

    def get_val(self, val: str | T) -> int:
        return (
            int(val) if isinstance(val, str) and val.isdigit() else self.registers[val]
        )

    def _should_continue(self) -> bool:
        return 0 <= self.ip < len(self.operations)

    def __getitem__(self, reg: T) -> int:
        return self.get_val(reg)

    def __setitem__(self, reg: T, val: int):
        self.registers[reg] = val

    def __iadd__(self, jump: int):
        self.ip += jump
        return self

    def __isub__(self, jump: int):
        self.ip -= jump
        return self

    def __repr__(self):
        return f"Program({self.name}: {str(self.registers)})"
