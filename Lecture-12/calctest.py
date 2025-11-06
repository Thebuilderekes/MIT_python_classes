import pytest
from calculator import add, subtract, multiply, divide, power

# test_calculator.py
# --- Unit Tests for basic functionality ---

def test_add_positive_numbers():
    """Test addition of two positive integers."""
    assert add(10, 5) == 15

def test_add_negative_numbers():
    """Test addition of negative integers."""
    assert add(-1, -10) == -11

def test_add_float_and_integer():
    """Test addition involving a float and an integer."""
    assert add(2.5, 3) == 5.5

def test_subtract_numbers():
    """Test simple subtraction."""
    assert subtract(10, 5) == 5

def test_subtract_to_negative():
    """Test subtraction resulting in a negative number."""
    assert subtract(5, 10) == -5

def test_multiply_numbers():
    """Test simple multiplication."""
    assert multiply(3, 4) == 12

def test_multiply_by_zero():
    """Test multiplication by zero."""
    assert multiply(100, 0) == 0

def test_divide_numbers():
    """Test simple division."""
    assert divide(10, 2) == 5.0

def test_power_positive():
    """Test raising a positive base to a positive power."""
    assert power(2, 3) == 8

# --- Testing for Exceptions (Error Handling) ---

def test_divide_by_zero():
    """
    Tests that the 'divide' function correctly raises a ValueError
    when the divisor is zero.
    """
    # The 'pytest.raises' context manager expects the specified exception type
    # to be raised within its block. If the exception is not raised, the test fails.
    with pytest.raises(ValueError) as e:
        divide(10, 0)
    
    # Optionally, you can check the error message
    assert "Cannot divide by zero!" in str(e.value)

# --- Parametrized Testing (Good for Regression Testing) ---
# Parametrization allows running the same test function multiple times
# with different sets of input data, which is excellent for checking against
# a list of known good (or bad) inputs in regression testing.

@pytest.mark.parametrize(
    "x, y, expected",
    [
        (1, 2, 3),      # Test case 1: basic positive
        (-1, 1, 0),     # Test case 2: zero result
        (-5, -5, -10),  # Test case 3: basic negative
        (10, 0, 10),    # Test case 4: adding zero
    ]
)
def test_add_many_scenarios(x, y, expected):
    """
    Tests the 'add' function using multiple input pairs (x, y) 
    and verifies them against the expected results.
    """
    assert add(x, y) == expected

# --- A simple "integration" test (if this were part of a larger system) ---

def test_calculate_volume_from_formula():
    """
    Simulated integration test: uses multiple unit functions 
    to calculate a more complex formula, like a cube's surface area (6 * side^2).
    """
    side = 4
    
    # 1. Calculate side squared (using power function)
    side_squared = power(side, 2)
    assert side_squared == 16
    
    # 2. Multiply by 6 (using multiply function)
    surface_area = multiply(6, side_squared)
    
    # 3. Final assertion
    assert surface_area == 96
    
    # If any of the underlying functions (power, multiply) had a bug, 
    # this integration test would likely fail.
