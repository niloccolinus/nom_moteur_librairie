"""Tests for verifying proper Matrix functionality."""

from Mathy import Matrix3x3, TranslationMatrix3x3, RotationMatrix3x3, HomothetyMatrix3x3


# Example matrix 0
matrix0 = Matrix3x3(
    0, 0, 0,
    0, 0, 0,
    0, 0, 0
)

# Example matrix 1
matrix1 = Matrix3x3(
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
)

# Translation matrix example
matrix_t = TranslationMatrix3x3(2, 3)

# Rotation matrix example
matrix_r = RotationMatrix3x3(45)

# Homothety matrix example
matrix_h = HomothetyMatrix3x3(2)


def test_repr():
    """Test __repr__() method."""
    # Repr matrix
    assert matrix0.__repr__() == "Matrix3x3([\n [0, 0, 0],\n [0, 0, 0],\n [0, 0, 0]\n])"  # noqa: E501


def test_add():
    """Test add() method."""
    # Add ints
    assert matrix0.add(matrix1) == Matrix3x3(1, 2, 3, 4, 5, 6, 7, 8, 9)
