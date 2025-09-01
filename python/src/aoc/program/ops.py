import operator
from typing import Callable, Generic

from attrs import define

from aoc.program import Operation, P


@define
class Assign(Operation[P], Generic[P]):
    reg: str
    val: int

    def __repr__(self):
        return f"Assign ({self.reg} := {self.val})"

    def execute(self, program: P):
        program[self.reg] = program.get_val(self.val)

@define
class BinaryOp(Operation[P], Generic[P]):
    reg: str
    left: int
    right: int

    op: Callable[[int, int], int]
    op_repr: str

    def __repr__(self):
        return f"{self.__class__.__name__} ({self.reg} = {self.left} {self.op_repr} {self.right})"

    def execute(self, program: P):
        program[self.reg] = self.op(program.get_val(self.left), program.get_val(self.right))


class Add(BinaryOp[P]):
    def __init__(self, reg: str, left: int, right: int):
        super().__init__(reg, left, right, operator.add, '+')
class Sub(BinaryOp[P]):
    def __init__(self, reg: str, left: int, right: int):
        super().__init__(reg, left, right, operator.sub, '-')
class Mul(BinaryOp[P]):
    def __init__(self, reg: str, left: int, right: int):
        super().__init__(reg, left, right, operator.mul, '*')
class Div(BinaryOp[P]):
    def __init__(self, reg: str, left: int, right: int):
        super().__init__(reg, left, right, operator.floordiv, '//')
class Mod(BinaryOp[P]):
    def __init__(self, reg: str, left: int, right: int):
        super().__init__(reg, left, right, operator.mod, '%')
class BitAnd(BinaryOp[P]):
    def __init__(self, reg: str, left: int, right: int):
        super().__init__(reg, left, right, operator.and_, '&')
class BitOr(BinaryOp[P]):
    def __init__(self, reg: str, left: int, right: int):
        super().__init__(reg, left, right, operator.or_, '|')


@define
class IncrementalOp(Operation[P], Generic[P]):
    reg: str
    val: int

    op: Callable[[int, int], int]
    op_repr: str

    def __repr__(self):
        return f"{self.__class__.__name__} ({self.reg} {self.op_repr}= {self.val})"

    def execute(self, program: P):
        program[self.reg] = self.op(program.get_val(self.reg), program.get_val(self.val))

class IAdd(BinaryOp[P]):
    def __init__(self, reg: str, left: int, right: int):
        super().__init__(reg, left, right, operator.add, '+')
class ISub(BinaryOp[P]):
    def __init__(self, reg: str, left: int, right: int):
        super().__init__(reg, left, right, operator.sub, '-')
class IMul(BinaryOp[P]):
    def __init__(self, reg: str, left: int, right: int):
        super().__init__(reg, left, right, operator.mul, '*')
class IDiv(BinaryOp[P]):
    def __init__(self, reg: str, left: int, right: int):
        super().__init__(reg, left, right, operator.floordiv, '//')
class IMod(BinaryOp[P]):
    def __init__(self, reg: str, left: int, right: int):
        super().__init__(reg, left, right, operator.mod, '%')
class IBitAnd(BinaryOp[P]):
    def __init__(self, reg: str, left: int, right: int):
        super().__init__(reg, left, right, operator.and_, '&')
class IBitOr(BinaryOp[P]):
    def __init__(self, reg: str, left: int, right: int):
        super().__init__(reg, left, right, operator.or_, '|')


@define
class Jump(Operation[P], Generic[P]):
    cmp: Callable[[int, int], bool]
    left: str | int
    right: str | int
    jump: str | int

    def __repr__(self):
        return f"Jump ({self.jump} if {self.left} {repr(self.cmp)} {self.right})"

    def advance(self, program: P):
        first = program.get_val(self.left)
        second = program.get_val(self.right)

        should_jump = self.cmp(first, second)
        program += program.get_val(self.jump) if should_jump else 1
