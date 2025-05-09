"""Defines a triangle class."""

import math


class Triangle:
    """A class to represent a triangle."""

    def __init__(
        self,
        p1: tuple[float, float],
        p2: tuple[float, float],
        p3: tuple[float, float]
    ):
        """
        Initialize a triangle with 3 vertices.
        Each point is a tuple (x, y).
        """
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def side_lengths(self) -> tuple[float, float, float]:
        """
        Return the lengths of the triangle's sides (a, b, c) where:
            a = length between p1 and p2
            b = length between p2 and p3
            c = length between p1 and p3
        """
        def distance(pA, pB):
            dx = pA[0] - pB[0]
            dy = pA[1] - pB[1]
            return math.sqrt(dx ** 2 + dy ** 2)

        a = distance(self.p1, self.p2)
        b = distance(self.p2, self.p3)
        c = distance(self.p1, self.p3)
        return a, b, c

    def perimeter(self) -> float:
        """
        Return the perimeter of the triangle.
        """
        a, b, c = self.side_lengths()
        return a + b + c

    def area(self) -> float:
        """
        Return the area of the triangle using Heron's formula.
        """
        if self.right_angled():
            # Sort to make sure the hypothenuse is last
            a, b, c = sorted(self.side_lengths())
            return ((a * b) / 2)
        a, b, c = self.side_lengths()
        s = (a + b + c) / 2  # semi-perimeter
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    def right_angled(self) -> bool:
        """
        Check if the triangle is a right triangle using Pythagorean theorem.
        """
        # Sort to make sure the hypothenuse is last
        a, b, c = sorted(self.side_lengths())
        # Use isclose to allow for small floating-point errors
        return math.isclose(a ** 2 + b ** 2, c ** 2, rel_tol=1e-9)

    def get_vertices(
        self
    ) -> tuple[tuple[float, float], tuple[float, float], tuple[float, float]]:
        """
        Return the three vertices of the triangle.
        """
        return self.p1, self.p2, self.p3
