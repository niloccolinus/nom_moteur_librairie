"""Tests for verifying proper Matrix functionality."""

import pytest
from Mathy import (
    Matrix3x3,
    TranslationMatrix3x3,
    RotationMatrix3x3,
    HomothetyMatrix3x3,
    deg, sin, cos
)

# Example matrix 0 (zero matrix)
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
    assert matrix0.__repr__() == "Matrix3x3([\n [0, 0, 0],\n [0, 0, 0],\n [0, 0, 0]\n])"  # noqa: E501


def test_eq():
    """Test __eq__() method."""
    assert matrix0 == Matrix3x3(
        0, 0, 0,
        0, 0, 0,
        0, 0, 0
    )
    assert matrix1 != matrix2


def test_add():
    """Test add() method with valid and invalid inputs."""
    result = matrix0.add(matrix1)
    assert result == matrix1

    result = matrix1.add(matrix2)
    expected = Matrix3x3(
        10, 10, 10,
        10, 10, 10,
        10, 10, 10
    )
    assert result == expected

    # Invalid type
    with pytest.raises(TypeError):
        matrix1.add("not a matrix")


def test_prod_r():
    """Test prod_r() method."""
    assert matrix1.prod_r(0) == matrix0
    result = matrix1.prod_r(2)
    expected = Matrix3x3(
        2, 4, 6,
        8, 10, 12,
        14, 16, 18
    )
    assert result == expected


def test_prod():
    """Test prod() method with valid and invalid inputs."""
    result = matrix1.prod(matrix2)
    expected = Matrix3x3(
        30, 24, 18,
        84, 69, 54,
        138, 114, 90
    )
    assert result == expected

    # Invalid type
    with pytest.raises(TypeError):
        matrix1.prod("invalid")


def test_determinant():
    """Test determinant() method."""
    assert matrix1.determinant() == 0
    m = Matrix3x3(
        1, 2, 3,
        0, 1, 4,
        5, 6, 0
    )
    assert abs(m.determinant() - 1) < 1e-6
