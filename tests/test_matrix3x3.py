"""Tests for verifying proper Matrix functionality."""

from Mathy import Matrix3x3, TranslationMatrix3x3, RotationMatrix3x3, HomothetyMatrix3x3  # noqa: E501


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

# Example matrix 2
matrix2 = Matrix3x3(
    9, 8, 7,
    6, 5, 4,
    3, 2, 1
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
    assert matrix0.add(matrix1) == Matrix3x3(
        1, 2, 3, 
        4, 5, 6, 
        7, 8, 9
    )


def test_prod_r():
    """Test prod_r() method."""
    # Multiply by zero
    assert matrix1.prod_r(0).matrix == matrix0.matrix
    # Multiply by non-zero scalar
    assert matrix1.prod_r(2).matrix == Matrix3x3(
        2, 4, 6, 
        8, 10, 12, 
        14, 16, 18
    ).matrix


def test_prod():
    """Test prod() method."""
    # Multiply by matrix
    assert matrix1.prod(matrix2).matrix == Matrix3x3(
        30, 24, 18, 
        84, 69, 54,
        138, 114, 90
    ).matrix
