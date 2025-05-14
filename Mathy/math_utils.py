pi = 3.1415926535897932384626433832795028841971  # Value of constant pi


def factorial(n):
    """Factorial Function"""
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def deg(x):
    """Convert degrees to radians"""
    rad = x * pi/180
    return rad


def sin(x):
    """Use Taylor Expansion to approximate sin x"""
    k = 0
    sinx = 0
    while x >= pi:
        x -= pi
    if pi > x > pi / 2:
        x = pi - x
    while k < 15:
        sinx += (-1)**k * x**(2*k + 1) / factorial(2*k + 1)
        k += 1
    return sinx


def cos(x):
    """Use sin x to calculate cos x"""
    cosx = sin(pi / 2 - x)
    return cosx
