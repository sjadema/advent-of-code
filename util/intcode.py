import operator
from typing import List


class IntCode:
    INSTRUCTIONS = {
        1: 4,
        2: 4,
        99: 1
    }

    OPERATORS = {
        1: getattr(operator, 'add'),
        2: getattr(operator, 'mul'),
    }

    def __init__(self, instructions: List[int]):
        self.instructions = instructions.copy()
        self.pointer = 0

    def run(self) -> int:
        while True:
            if self.pointer >= len(self.instructions):
                raise RuntimeError('Invalid instructions.')

            op_code = self.instructions[self.pointer]
            if 99 == op_code:
                break

            left = self.instructions[self.pointer + 1]
            right = self.instructions[(self.pointer + 2)]
            target = self.instructions[self.pointer + 3]

            self.instructions[target] = self.__execute(op_code, self.instructions[left], self.instructions[right])

            self.pointer += self.INSTRUCTIONS[op_code]

        return self.instructions[0]

    def __execute(self, op_code: int, left: int, right: int) -> int:
        operation = self.OPERATORS[op_code]

        return operation(left, right)

