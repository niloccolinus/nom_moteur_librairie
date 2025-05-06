"""Defines a two-vector class."""

from geometry_engine_librairie.Mathy.matrix2x2 import Matrix2x2



class Vector2:
    """A class to represent a bivector."""

    def __init__(self, x: float | int, y: float | int):
        """Initialize a 2D vector with the given x and y components."""
        self.x = x
        self.y = y

    @property
    def norm(self) -> float:
        """Calculate the norm of the vector (accessible as a property)."""
        return (self.x**2 + self.y**2)**0.5

    def __repr__(self):
        """Return a string representation of the vector."""
        return f"Vector2({self.x}, {self.y})"

    def add(self, other: 'Vector2') -> 'Vector2':
        """Add two vectors together and return a new Vector2."""
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        else:
            raise TypeError(f"{other} is not a Vector2")

    def subtract(self, other: 'Vector2') -> 'Vector2':
        """
        Subtract another vector from the current vector.

        Return the result as a new Vector2.
        """
        if isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        else:
            raise TypeError(f"{other} is not a Vector2")

    def scalar_product(self, other: 'Vector2') -> float:
        """Calculate the scalar (dot) product of two vectors."""
        if isinstance(other, Vector2):
            return self.x * other.x + self.y * other.y
        else:
            raise TypeError(f"{other} is not a Vector2")

    def multiply_by_scalar(self, factor: float | int) -> 'Vector2':
        """Multiply the vector by a scalar and return the resulting Vector2."""
        return Vector2(self.x * factor, self.y * factor)

    def multiply_by_matrix(self, matrix: 'Matrix2x2') -> 'Vector2':
        """
        Multiply the vector by a 2x2 matrix.

        Return the resulting Vector2.
        """
        from geometry_engine_librairie.Mathy.matrix2x2 import Matrix2x2
        if isinstance(matrix, Matrix2x2):
            a = matrix.matrix
            new_x = a[0][0] * self.x + a[0][1] * self.y
            new_y = a[1][0] * self.x + a[1][1] * self.y
            return Vector2(new_x, new_y)
        else:
            raise TypeError(f"{matrix} is not a Matrix2x2")

    def change_basis(self, base_v1: 'Vector2',
                     base_v2: 'Vector2') -> 'Vector2':
        """
        Implement a change of basis.

        Change the vector's basis from the standard basis to a new basis.
        """
        base_matrix = Matrix2x2(
            base_v1.x, base_v2.x,
            base_v1.y, base_v2.y
        )
        # Solve the system of equations to get the vector in the new basis
        return base_matrix.solve_system(self)

    def normalize(self) -> 'Vector2':
        """
        Normalize the vector to have a length of 1 while preserving its direction.
        """
        n = self.norm
        if n == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return Vector2(self.x / n, self.y / n)
