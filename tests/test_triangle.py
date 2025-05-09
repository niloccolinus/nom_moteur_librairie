"""Tests for the Triangle class."""


import math
from Mathy import Triangle

# Example triangle 1
triangle1 = Triangle([0, 0], [0, 1], [1, 0])
# Example triangle 2
triangle2 = Triangle([-1, 0], [0, 1], [1, 0])
# Example triangle 3
triangle3 = Triangle([-2.5, 0], [0, 5.5], [2.5, 0])


def test_side_lengths():
    # Lengths triangle 1
    assert triangle1.side_lengths() == (1.0, math.sqrt(2), 1.0)
    # Lengths triangle 2
    assert triangle2.side_lengths() == (math.sqrt(2), math.sqrt(2), 2.0)
    # Lengths triangle 3
    assert triangle3.side_lengths() == (math.sqrt(36.5), math.sqrt(36.5), 5.0)


def test_perimeter():
    # Perimeter triangle 1
    assert triangle1.perimeter() == float(2 + math.sqrt(2))
    # Perimeter triangle 2
    assert triangle2.perimeter() == float(2 + math.sqrt(2) * 2)
    # Perimeter triangle 3
    assert triangle3.perimeter() == float(5 + math.sqrt(36.5) * 2)


def test_area():
    # Area triangle 1
    assert triangle1.area() == 0.5
    # Area triangle 2
    assert math.isclose(triangle2.area(), 1.0)
    # Area triangle 3
    assert math.isclose(triangle3.area(), 13.75)


def test_right_angled():
    # Test right-angled triangle 1
    assert triangle1.right_angled() == 1
    # Test right-angled triangle 2
    assert triangle2.right_angled() == 1
    # Test non-right-angled triangle 3
    assert triangle3.right_angled() == 0


def test_get_vertices():
    # Vertices triangle 1
    assert triangle1.get_vertices() == ([0, 0], [0, 1], [1, 0])
    # Vertices triangle 2
    assert triangle2.get_vertices() == ([-1, 0], [0, 1], [1, 0])
    # Vertices triangle 3
    assert triangle3.get_vertices() == ([-2.5, 0], [0, 5.5], [2.5, 0])
