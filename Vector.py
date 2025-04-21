
class Vector:
    def __init__(self, term_1: float | int, term_2: float | int):
        self.term_1 = term_1
        self.term_2 = term_2
        self.vector = [self.term_1, self.term_2]

    def multiply_float(self, factor: float | int):
        result = Vector(0, 0)
        result.term_1 = self.term_1 * factor
        result.term_2 = self.term_2 * factor
        return result.vector

    def add_vector(self, vector_2: Vector):
        a = self.term_1 + vector_2.term_1
        b = self.term_2 + vector_2.term_2
        result = Vector(a, b)
        return result

    def substract_vector(self, vector_2: Vector):
        a = self.term_1 - vector_2.term_1
        b = self.term_2 - vector_2.term_2
        result = Vector(a, b)
        return result


