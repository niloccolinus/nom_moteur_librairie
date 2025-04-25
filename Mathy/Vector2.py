from matrix2x2 import Matrix2x2


class Vector2:
    def __init__(self, x: float | int, y: float | int):
        self.x, self.y = x, y
        self.vector = [self.x, self.y]
        self.norm = (self.x**2 + self.y**2)**0.5

    def set_x(self, x: int | float) -> None:
        self.x = x

    def set_y(self, y: int | float) -> None:
        self.y = y

    def get_x(self) -> int | float:
        return self.x

    def get_y(self) -> int | float:
        return self.y

    def get_norm(self) -> int | float:
        return self.norm

    def add(self, vector_2):
        if (isinstance(vector_2, Vector2)):
            result = Vector2(0, 0)
            result.set_x(self.x + vector_2.x)
            result.set_y(self.y + vector_2.y)
            return result.vector
        else:
            raise TypeError('{vector_2} is not a Vector2')

    def substract(self, vector_2):
        if (isinstance(vector_2, Vector2)):
            result = Vector2(0, 0)
            result.set_x(self.x - vector_2.x)
            result.set_y(self.y - vector_2.y)
            return result.vector
        else:
            raise TypeError('{vector_2} is not a Vector2')

    def multiply_by_scalar(self, factor: float | int):
        result = Vector2(0, 0)
        result.set_x(self.x * factor)
        result.set_y(self.y * factor)
        return result.vector

    def scalar_product(self, vector_2) -> int | float:
        if (isinstance(vector_2, Vector2)):
            result = self.x * vector_2.x + self.y * vector_2.y
            return result
        else:
            raise TypeError('{vector_2} is not a Vector2')

    def multiply_by_square_matrix(self, matrix: Matrix2x2):
        if (isinstance(matrix, Matrix2x2)):
            result = Vector2(0, 0)
            result.set_x(self.x * matrix.x1 + self.y * matrix.x2)
            result.set_y(self.x * matrix.x3 + self.y * matrix.x4)
            return result.vector
        else:
            raise TypeError('{matrix} is not a Matrix2x2')

    # To do:
    # ajouter méthode changement de base
