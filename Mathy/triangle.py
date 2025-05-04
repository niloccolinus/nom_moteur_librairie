class Triangle:
    def __init__(self, p1: tuple[float, float], p2: tuple[float, float], p3: tuple[float, float]):
        """
        Initialize a triangle with 3 vertices.
        Each point is a tuple (x, y).
        """
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3