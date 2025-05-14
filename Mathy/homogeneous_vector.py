"""Defines a two-vector class with homogeneous coordinates."""


class HomogeneousVector:
    """A class to represent a 2D vector."""

    def __init__(self, x: float | int, y: float | int):
        """Initialize a 2D vector with the given x and y components."""
        self.x = x
        self.y = y
        self.z = 1

    @property
    def norm(self) -> float:
        """Calculate the norm of the vector (accessible as a property)."""
        return (self.x**2 + self.y**2)**0.5

    def __eq__(self, other: 'HomogeneousVector') -> bool:
        """Check if two vectors are equal."""
        if isinstance(other, HomogeneousVector):
            return (self.x == other.x) and (self.y == other.y)
        else:
            raise TypeError(f"{other} is not a HomogeneousVector")

    def __repr__(self):
        """Return a string representation of the vector."""
        return f"HomogeneousVector({self.x}, {self.y})"

    def add(self, other: 'HomogeneousVector') -> 'HomogeneousVector':
        """Add two vectors together and return a new HomogeneousVector."""
        if isinstance(other, HomogeneousVector):
            return HomogeneousVector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError(f"{other} is not a HomogeneousVector")

    def subtract(self, other: 'HomogeneousVector') -> 'HomogeneousVector':
        """
        Subtract another vector from the current vector.

        Return the result as a new HomogeneousVector.
        """
        if isinstance(other, HomogeneousVector):
            return HomogeneousVector(self.x - other.x, self.y - other.y)
        else:
            raise TypeError(f"{other} is not a HomogeneousVector")

    def scalar_product(self, other: 'HomogeneousVector') -> float:
        """Calculate the scalar (dot) product of two vectors."""
        if isinstance(other, HomogeneousVector):
            return self.x * other.x + self.y * other.y
        else:
            raise TypeError(f"{other} is not a HomogeneousVector")

    def multiply_by_scalar(self, factor: float | int) -> 'HomogeneousVector':
        """Multiply by a scalar and return the resulting HomogeneousVector."""
        return HomogeneousVector(self.x * factor, self.y * factor)

    def multiply_by_matrix(self, matrix) -> 'HomogeneousVector':
        """
        Multiply the vector by a 2x2 matrix.

        Return the resulting HomogeneousVector.
        """
        from Mathy import Matrix2x2
        if isinstance(matrix, Matrix2x2):
            a = matrix.matrix
            new_x = a[0][0] * self.x + a[0][1] * self.y
            new_y = a[1][0] * self.x + a[1][1] * self.y
            return HomogeneousVector(new_x, new_y)
        else:
            raise TypeError(f"{matrix} is not a Matrix2x2")

    def change_basis(self, base_v1: 'HomogeneousVector',
                     base_v2: 'HomogeneousVector') -> 'HomogeneousVector':
        """
        Implement a change of basis.

        Change the vector's basis from the standard basis to a new basis.
        """
        from Mathy import Matrix2x2
        base_matrix = Matrix2x2(
            base_v1.x, base_v2.x,
            base_v1.y, base_v2.y
        )
        # Solve the system of equations to get the vector in the new basis
        return base_matrix.solve_system(self)

    def normalize(self) -> 'HomogeneousVector':
        """
        Normalize the vector.

        The new vector has the same direction and a length of 1.
        """
        n = self.norm
        if n == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return HomogeneousVector(self.x / n, self.y / n)
