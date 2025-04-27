from matrix2x2 import Matrix2x2


class Vector2:
    def __init__(self, x: float | int, y: float | int):
        self.x = x
        self.y = y

    @property
    def norm(self) -> float:
        return (self.x**2 + self.y**2)**0.5

    def __repr__(self):
        return f"Vector2({self.x}, {self.y})"

    def add(self, other: 'Vector2') -> 'Vector2':
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        else:
            raise TypeError(f"{other} is not a Vector2")

    def subtract(self, other: 'Vector2') -> 'Vector2':
        if isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        else:
            raise TypeError(f"{other} is not a Vector2")

    def scalar_product(self, other: 'Vector2') -> float:
        if isinstance(other, Vector2):
            return self.x * other.x + self.y * other.y
        else:
            raise TypeError(f"{other} is not a Vector2")

    def multiply_by_scalar(self, factor: float | int) -> 'Vector2':
        return Vector2(self.x * factor, self.y * factor)

    def multiply_by_matrix(self, matrix: Matrix2x2) -> 'Vector2':
        if isinstance(matrix, Matrix2x2):
            a = matrix.matrix
            new_x = a[0][0] * self.x + a[0][1] * self.y
            new_y = a[1][0] * self.x + a[1][1] * self.y
            return Vector2(new_x, new_y)
        else:
            raise TypeError(f"{matrix} is not a Matrix2x2")

    # To do:
    # ajouter méthode changement de base
