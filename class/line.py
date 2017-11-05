from typing import Optional


class Line:

    def __init__(self, start: tuple, end: tuple) -> None:
        self.start = start
        self.end = end

    def get_start(self) -> tuple:
        """
        Returns the coordinates of the start of the line.
        :return: A tuple containing the start coordinates.
        """
        return self.start

    def get_end(self) -> tuple:
        """
        Returns the coordinates of the end of the line.
        :return: A tuple containing the end coordinates.
        """
        return self.end

    def get_length(self) -> float:
        """
        Returns the length of the line.
        :return: The length of the line.
        """
        x = (self.end[0] - self.start[0]) ** 2
        y = (self.end[1] - self.start[1]) ** 2
        return (x + y) ** .5

    def has_intersection(self, line: 'Line') -> Optional[tuple]:
        """
        Calculates if the provided line intersects with this line. (http://paulbourke.net/geometry/pointlineplane/#i2l)
        :param line: The line to check for intersection
        :return: A tuple when the lines intersect, None otherwise
        """

        # Line a
        x1 = self.start[0]
        y1 = self.start[1]

        x2 = self.end[0]
        y2 = self.end[1]

        # Line b
        x3 = line.get_start()[0]
        y3 = line.get_start()[1]

        x4 = line.get_end()[0]
        y4 = line.get_end()[1]

        denominator = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
        if denominator == 0:
            return None

        nominator_a = (x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)
        nominator_b = (x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)

        unknown_a = nominator_a / denominator
        unknown_b = nominator_b / denominator

        if 0 <= unknown_a <= 1 and 0 <= unknown_b <= 1:
            return (x1 + (unknown_a * (x2 - x1)), y1 + unknown_a * (y2 - y1))

        return None

