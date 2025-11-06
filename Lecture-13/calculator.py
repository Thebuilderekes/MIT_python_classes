# def multiply(a, b):
#     return a * b
#
# def test_multiply_positive():
#     assert multiply(3, 4) == 12
#
# def test_multiply_negative():
#     assert multiply(-2, 3) == -6
#
# def test_multiply_zero():
#     assert multiply(0, 100) == 0
#
# calculator.py

"""
A simple module containing basic arithmetic functions
to demonstrate unit testing with pytest.
"""


def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """
    Returns the division of two numbers.
    Raises ValueError if the divisor (b) is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def power(a, b):
    """Returns a raised to the power of b."""
    return a ** b
