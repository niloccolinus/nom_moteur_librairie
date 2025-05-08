"""Tests for verifying proper Vector functionality."""

import pytest
from Mathy.vector2 import Vector2
from Mathy.matrix2x2 import Matrix2x2


def test_norm():
    # Norm zero
    assert Vector2(0, 0).norm == 0.0

    # Norm positive coordinates
    assert round(Vector2(2, 4).norm, 2) == 4.47

    # Norm negative coordinates
    assert round(Vector2(-2, -4).norm, 2) == 4.47


def test_eq():
    # Compare different vectors
    assert Vector2(1, 1) != Vector2(1, -1)
    # Compare same vectors
    assert Vector2(1, 1) == Vector2(1, 1)
    # Compare a vector with a different type
    with pytest.raises(TypeError, match=r".* is not a Vector2.*"):
        Vector2(1, 2) != 5


def test_repr():
    # Repr vector
    assert Vector2(1, 3).__repr__() == "Vector2(1, 3)"


def test_add():
    # Add zeros
    assert Vector2(0, 0).add(Vector2(0, 0)) == Vector2(0, 0)

    # Add ints
    assert Vector2(1, 2).add(Vector2(3, -4)) == Vector2(4, -2)

    # Add floats
    assert Vector2(0.5, -1.0).add(Vector2(3.5, 5.0)) == Vector2(4.0, -2.0)

    # Add wrong type
    with pytest.raises(TypeError, match=r".* is not a Vector2.*"):
        Vector2(1, 2).add(-4)


def test_subtract():
    # Subtract zeros
    assert Vector2(0, 0).subtract(Vector2(0, 0)) == Vector2(0, 0)

    # Subtract ints
    assert Vector2(1, 2).subtract(Vector2(3, -4)) == Vector2(-3, 6)

    # Subtract floats
    assert Vector2(0.5, -1.0).subtract(Vector2(3.5, 5.0)) == Vector2(-3.0, -6.0)

    # Subtract wrong type
    with pytest.raises(TypeError, match=r".* is not a Vector2.*"):
        Vector2(1, 2).subtract(-4)


def test_scalar_product():
    # Scalar product of v1 = [1, 1] and v2 = [1, -1]
    assert Vector2(1, 1).scalar_product(Vector2(1, -1)) == 0
    # Use wrong type
    with pytest.raises(TypeError, match=r".* is not a Vector2.*"):
        Vector2(1, 1).scalar_product(0)


def test_multiply_by_scalar():
    # Multiply by 0
    assert Vector2(1, 1).multiply_by_scalar(0) == Vector2(0, 0)
    # Multiply by int
    assert Vector2(1, 1).multiply_by_scalar(2) == Vector2(2, 2)
    # Multiply by float
    assert Vector2(1, 1).multiply_by_scalar(0.5) == Vector2(0.5, 0.5)


def test_multiply_by_matrix():
    # Multiply by matrix
    assert Vector2(3, -4).multiply_by_matrix(Matrix2x2(2, 3, 4, -1)) == Vector2(-6, 16)
    # Multiply by wrong type
    with pytest.raises(TypeError, match=r".* is not a Matrix2x2.*"):
        Vector2(3, -4).multiply_by_matrix(Vector2(2, 3))


def test_change_basis():
    # Change basis
    assert Vector2(2, 3).change_basis(Vector2(1, 1), Vector2(1, -1)) == Vector2(2.5, -0.5)


def test_normalize():
    # Normalize vector
    assert Vector2(1, 0).normalize() == Vector2(1.0, 0.0)
    # Norm == 0
    with pytest.raises(ValueError, match=r"Cannot normalize a zero vector.*"):
        Vector2(0, 0).normalize()
