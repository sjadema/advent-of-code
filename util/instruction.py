import operator
import re


class Instruction:

    OPERATORS = {
        '<': getattr(operator, 'lt'),
        '>': getattr(operator, 'gt'),
        '<=': getattr(operator, 'le'),
        '>=': getattr(operator, 'ge'),
        '==': getattr(operator, 'eq'),
        '!=': getattr(operator, 'ne'),
    }

    def __init__(self, register: str, operation: str, value: int, condition: str):
        self.register = register
        self.operation = operation
        self.value = value
        self.condition = condition

        match = re.search('^(?P<register>[\w]+) (?P<operator>[^ ]+) (?P<value>[\d-]+)$', condition)
        self.target_register = match.group('register')
        self.operator = self.OPERATORS[match.group('operator')]
        self.target_value = int(match.group('value'))

    def get_register(self) -> str:
        return self.register

    def get_operation(self) -> str:
        return self.operation

    def get_value(self) -> int:
        return self.value

    def get_condition(self) -> str:
        return self.condition

    def get_target_register(self) -> str:
        return self.target_register

    def get_target_value(self) -> int:
        return self.target_value

    def get_operator(self):
        return self.operator
