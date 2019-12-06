from __future__ import annotations
from typing import List, Callable


class IntCode:
    OP_CODE_LENGTHS = {
        1: 4,
        2: 4,
        3: 2,
        4: 2,
        99: 1,
    }

    def __init__(self, instructions: List[int], inputs: List[int] = None) -> None:
        self.instructions = instructions.copy()
        self.inputs = inputs[::-1] if inputs is not None else []

        self.__running = False
        self.pointer = 0
        self.output = ''

    def run(self) -> IntCode:
        self.__running = True

        while self.__running:
            try:
                instruction = self.instructions[self.pointer]
            except KeyError:
                raise RuntimeError('Invalid instructions.')

            # Determine op code & operation
            op_code = self.__get_op_code(instruction)
            operation = self.__get_operation(op_code)

            # Determine modes & parameters for operation
            args = []
            modes = self.__get_modes(instruction)
            for i in range(self.pointer + 1, self.pointer + self.OP_CODE_LENGTHS[op_code]):
                mode = modes.pop()
                args.append(self.__get_value(mode, self.instructions[i]))

            operation(*tuple(args))

            self.pointer += self.OP_CODE_LENGTHS[op_code]

        return self

    def result(self, address: int) -> int:
        return self.instructions[address]

    @staticmethod
    def __normalize_instruction(instruction: int) -> str:
        instruction = f"{instruction:04}"

        return '1' + instruction

    @staticmethod
    def __get_op_code(instruction: int) -> int:
        instruction = IntCode.__normalize_instruction(instruction)

        return int(instruction[-2:])

    @staticmethod
    def __get_modes(instruction: int) -> List[int]:
        instruction = IntCode.__normalize_instruction(instruction)

        return [int(mode) for mode in instruction[0:3]]

    def __get_operation(self, op_code: int) -> Callable:
        operators = {
            1: self.__add,
            2: self.__mul,
            3: self.__input,
            4: self.__output,
            99: self.__terminate,
        }

        return operators[op_code]

    def __get_value(self, mode: int, address: int):
        return self.instructions[address] if 0 == mode else address

    def __add(self, left: int, right: int, address: int) -> None:
        self.instructions[address] = left + right

    def __mul(self, left: int, right: int, address: int) -> None:
        self.instructions[address] = left * right

    def __input(self, address: int) -> None:
        self.instructions[address] = self.inputs.pop()

    def __output(self, value: int) -> None:
        self.output += value

    def __terminate(self) -> None:
        self.__running = False

    def output(self):
        return self.output
