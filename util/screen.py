from copy import deepcopy


class Screen:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.screen = []
        for i in range(0, height):
            self.screen.append(['.'] * width)

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height

    def draw_rect(self, width: int, height: int):
        for row in range(0, height):
            for column in range(0, width):
                self.screen[row][column] = '#'

    def rotate_col(self, column: int, amount: int):
        original_screen = deepcopy(self.screen)
        for row in range(0, self.get_height()):
            self.screen[(row + amount) % self.get_height()][column] = original_screen[row][column]

    def rotate_row(self, row: int, amount: int):
        original_screen = deepcopy(self.screen)
        for column in range(0, self.get_width()):
            self.screen[row][(column + amount) % self.get_width()] = original_screen[row][column]

    def get_active(self) -> int:
        active = 0
        for row in self.screen:
            for column in row:
                if '#' == column:
                    active += 1

        return active

    def get_inactive(self) -> int:
        return self.get_width() * self.get_height() - self.get_active()

    def get_display(self) -> [[]]:
        return self.screen

    def __str__(self):
        lines = ''
        for row in self.get_display():
            line = ''
            for column in row:
                line += column

            lines += line + '\n'

        return lines
