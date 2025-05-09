"""Tests for the Triangle class."""

import pytest
from Mathy import Triangle

# Example triangle 1
triangle1 = Triangle([0, 0], [0, 1], [1, 0])


def test_side_lengths():
    # Lengths triangle 1
    assert triangle1.side_lengths() == (1.0, float(2**0.5), 1.0)


def test_perimeter():
    # Perimeter triangle 1
    assert triangle1.perimeter() == float(2 + 2**0.5)


def test_area():
    # Area triangle 1
    assert triangle1.area() == 0.5


def test_right_angled():
    # Test right-angled triangle
    assert triangle1.right_angled() == 1


def test_get_vertices():
    assert triangle1.get_vertices() == ([0, 0], [0, 1], [1, 0])
