from __future__ import annotations
from typing import List, Callable, Optional


class IntCode:
    OP_CODE_DEFAULTS = {
        1: [0, 0, 1],
        2: [0, 0, 1],
        3: [1],
        4: [0],
        5: [0, 0],
        6: [0, 0],
        7: [0, 0, 1],
        8: [0, 0, 1],
        9: [1],
        99: [],
    }

    def __init__(self, instructions: List[int], inputs: List[int] = None) -> None:
        self.instructions = instructions.copy()

        self.inputs = inputs.copy()[::-1] if inputs is not None else []

        self.__running = False
        self.__increase_pointer = True
        self.__base = 0

        self.pointer = 0
        self.output = ''

    def run(self) -> IntCode:
        self.__running = True

        while self.__running:
            try:
                instruction = self.instructions[self.pointer]
            except IndexError:
                raise RuntimeError('Invalid instructions.')

            # Determine op code & operation
            op_code = self.__get_op_code(instruction)
            operation = self.__get_operation(op_code)

            # Determine parameter length
            parameter_length = len(self.OP_CODE_DEFAULTS[op_code])

            # Determine modes & parameters for operation
            args = []
            modes = self.__get_modes(instruction)
            for i in range(self.pointer + 1, self.pointer + parameter_length + 1):
                mode = modes.pop()
                args.append(self.__get_value(mode, self.instructions[i]))

            operation(*tuple(args))

            if self.__increase_pointer:
                self.pointer += parameter_length + 1

            self.__increase_pointer = True

        return self

    def result(self, address: int) -> int:
        return self.instructions[address]

    @staticmethod
    def __normalize_instruction(instruction: int) -> str:
        op_str = f"{instruction:02}"[-2:]

        op_code = int(op_str)
        defaults = IntCode.OP_CODE_DEFAULTS[op_code]

        parameters = str(instruction)[::-1][2:]
        defined = list(parameters) if '' != parameters else []

        parameters = []
        for i in range(len(defaults)):
            try:
                parameter = defined[i]
            except IndexError:
                parameter = defaults[i]

            parameters.append(parameter)

        return ''.join([str(p) for p in parameters[::-1]]) + op_str

    @staticmethod
    def __get_op_code(instruction: int) -> int:
        instruction = IntCode.__normalize_instruction(instruction)

        return int(instruction[-2:])

    @staticmethod
    def __get_modes(instruction: int) -> List[int]:
        instruction = IntCode.__normalize_instruction(instruction)

        return [int(mode) for mode in instruction[0:-2]]

    def __get_operation(self, op_code: int) -> Callable:
        operations = {
            1: self.__add,
            2: self.__mul,
            3: self.__input,
            4: self.__output,
            5: self.__if_true,
            6: self.__if_false,
            7: self.__less_than,
            8: self.__equals,
            9: self.__offset_base,
            99: self.__terminate,
        }

        return operations[op_code]

    def __get_value(self, mode: int, address: int):
        if 1 == mode:
            return address

        if 2 == mode:
            address += self.__base

        return self.instructions[self.__access_memory(address)]

    def __access_memory(self, address: int):
        if len(self.instructions) <= address:
            # print(address, len(self.instructions), self.pointer)

            expand_by = [0] * (address - len(self.instructions) + 1)
            self.instructions += expand_by
            # print(len(self.instructions))

        return address

    def __add(self, left: int, right: int, address: int) -> None:
        self.instructions[self.__access_memory(address)] = left + right

    def __mul(self, left: int, right: int, address: int) -> None:
        self.instructions[self.__access_memory(address)] = left * right

    def __input(self, address: int) -> None:
        self.instructions[self.__access_memory(address)] = self.inputs.pop()

    def __output(self, value: int) -> None:
        self.output += str(value)

    def __if_true(self, value: int, position: int):
        if 0 != value:
            self.pointer = position
            self.__increase_pointer = False

    def __if_false(self, value: int, position: int):
        if 0 == value:
            self.pointer = position
            self.__increase_pointer = False

    def __less_than(self, left: int, right: int, address: int):
        self.instructions[self.__access_memory(address)] = 1 if left < right else 0

    def __equals(self, left: int, right: int, address: int):
        self.instructions[self.__access_memory(address)] = 1 if left == right else 0

    def __offset_base(self, value: int) -> None:
        self.__base += value

    def __terminate(self) -> None:
        self.__running = False

    def get_output(self) -> str:
        return self.output

    def get_instructions(self) -> List[int]:
        return self.instructions
