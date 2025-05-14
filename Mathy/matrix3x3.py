"""Defines a 3x3 matrix class."""

from Mathy import cos, sin


class Matrix3x3:
    """A class to represent a 3 by 3 matrix."""

    def __init__(self, x1: float | int, x2: float | int, x3: float | int,
                 x4: float | int, x5: float | int, x6: float | int,
                 x7: float | int, x8: float | int, x9: float | int):
        """Initialize a 3x3 matrix with the given values."""
        self.matrix = [[x1, x2, x3], [x4, x5, x6], [x7, x8, x9]]

    def __repr__(self):
        """Return a string representation of the matrix."""
        return f"Matrix3x3([\n {self.matrix[0]},\n {self.matrix[1]},\n {self.matrix[2]}\n])"  # noqa: E501


class TranslationMatrix3x3(Matrix3x3):
    """A class to represent a 3 by 3 translation matrix."""

    def __init__(self, a, b):
        super().__init__(
            1, 0, a,
            0, 1, b,
            0, 0, 1
        )
        self.a = a
        self.b = b


class RotationMatrix3x3(Matrix3x3):
    """A class to represent a 3 by 3 rotation matrix."""

    def __init__(self, t):
        super().__init__(
            cos(t), -sin(t), 0,
            sin(t), cos(t), 0,
            0, 0, 1
        )
        self.t = t
