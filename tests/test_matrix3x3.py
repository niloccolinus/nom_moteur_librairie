"""Tests for verifying proper Matrix functionality."""

from Mathy import Matrix3x3, TranslationMatrix3x3


# Example matrix 0
matrix0 = Matrix3x3(
    0, 0, 0,
    0, 0, 0,
    0, 0, 0
)

# Example matrix 1
matrix_t = TranslationMatrix3x3(2, 3)


def test_repr():
    """Test __repr__() method."""
    # Repr vector
    assert matrix_t.__repr__() == "Matrix3x3([\n [1, 0, 2],\n [0, 1, 3],\n [0, 0, 1]\n])"  # noqa: E501
