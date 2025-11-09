from calculator import divide, add

# assertion_and_exception_examples.py
# =======================================================
# SECTION 1: ASSERTIONS (Used for Sanity Checks & Testing)
# =======================================================

print("--- 1. Using assert for Sanity Checks (Development/Testing) ---")

def calculate_monthly_payment(loan_amount, rate, years):
    """
    A placeholder function where we must ensure inputs are valid.
    Assertions are best used for checking conditions that should NEVER happen
    if the code is working correctly.
    """
    # 1. Assert that the loan amount is positive
    assert loan_amount > 0, "Loan amount must be a positive value."

    # 2. Assert that the rate is within a reasonable range (0% to 100%)
    assert 0 <= rate <= 1.0, "Interest rate must be between 0 and 1 (0% and 100%)."

    # 3. Assert that years is an integer
    assert isinstance(years, int), "Years must be an integer."

    # If all assertions pass, the function proceeds (simplified calculation below)
    print(f"Inputs validated successfully: Amount=${loan_amount}")
    return loan_amount / (years * 12)

# Example 1: Successful Assertion (Program runs normally)
result_good = calculate_monthly_payment(10000, 0.05, 5)
print(f"Monthly payment (successful): {result_good:.2f}\n")

# Example 2: Failed Assertion (Program will immediately halt with an AssertionError)
# To see this fail, uncomment the lines below:
# print("Attempting to assert that a loan is impossible (will crash if uncommented)...")
# result_bad = calculate_monthly_payment(-500, 0.05, 5)
# print("This line will not be reached if the assertion fails!")


# =======================================================
# SECTION 2: EXCEPTION HANDLING (Used for Graceful Error Recovery)
# =======================================================

print("--- 2. Using try...except for Graceful Error Handling ---")
# We use the divide function from calculator.py, which raises a ValueError
# when dividing by zero.

numerator = 50
divisor_list = [5, 2, 'a', 10]
## the different errors used in except it in anticipation
#that those kinds of error will occur during the program so you would want to catch those
for divisor in divisor_list:
    try:
        # Tries to execute this block of code
        print(f"Attempting {numerator} / {divisor}...")
        result = divide(numerator, divisor)
        print(f"Success! Result: {result}")

    except ValueError as e:
        # Executes ONLY if a ValueError occurs in the try block
        print("Error Handled: Cannot calculate division.")
        print(f"Details: {e}") # Print the custom message from calculator.py

    except TypeError as e:
        print("cannot divide by divisor provided")

    finally:
        # Executes always, regardless of whether an exception occurred or not
        print("--- Next calculation attempt ---")

print("\nFinished all attempts, program continues.")


# =======================================================
# SECTION 3: ASSERTS IN TESTS (as seen in test_calculator.py)
# =======================================================

print("--- 3. Assertions in Pytest (Verifying Expected Results) ---")

# In testing, 'assert' is used to check if the actual output matches the expected output.

ACTUAL_SUM = add(7, 3)
EXPECTED_SUM = 10

# This is the standard form of a test assertion:
assert ACTUAL_SUM == EXPECTED_SUM, f"expected {EXPECTED_SUM}, but got {ACTUAL_SUM}"
print(f"Test Assertion Passed: {ACTUAL_SUM} equals {EXPECTED_SUM}")

# Assertion for a string comparison
CITY = "London"
assert CITY.startswith("L"), "City should start with 'L'"
print("String assertion passed.")
