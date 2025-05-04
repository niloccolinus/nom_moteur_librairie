import math

class Triangle:
    def __init__(self, p1: tuple[float, float], p2: tuple[float, float], p3: tuple[float, float]):
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
