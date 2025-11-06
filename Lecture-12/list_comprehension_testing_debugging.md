# Python: List Comprehension, Functions as Objects, and Testing & Debugging

## List Comprehension

List comprehension is a concise and efficient way to create new lists by applying an operation to each element of an existing list. It's more readable and faster than writing traditional for loops.

### Basic Syntax

The general syntax is: `[expression for item in iterable if condition]`

The `if condition` part is optional and filters which items to include.

### Simple Examples

Without list comprehension, you might write:
```python
squares = []
for x in range(5):
    squares.append(x ** 2)
# Result: [0, 1, 4, 9, 16]
```

With list comprehension, it becomes one line:
```python
squares = [x ** 2 for x in range(5)]
# Result: [0, 1, 4, 9, 16]
```

### With Conditions

You can filter items using an `if` clause:
```python
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
# Result: [0, 4, 16, 36, 64]
```

### Nested List Comprehensions

You can flatten nested lists or create matrices:
```python
# Flatten a nested list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
# Result: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create a 3x3 matrix of zeros
matrix = [[0 for _ in range(3)] for _ in range(3)]
# Result: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
```

### With Functions

List comprehensions work great with functions:
```python
def double(x):
    return x * 2

numbers = [1, 2, 3, 4, 5]
doubled = [double(x) for x in numbers]
# Result: [2, 4, 6, 8, 10]
```

### When NOT to Use List Comprehension

Avoid list comprehension when you have side effects (like printing) or when the logic becomes too complex and hard to read:
```python
# Bad: Using list comprehension just for side effects
[print(x) for x in range(5)]  # Creates a list of None values

# Good: Use a regular for loop instead
for x in range(5):
    print(x)
```

---

## Functions as Objects

In Python, functions are first-class objects, meaning they can be assigned to variables, passed as arguments, and returned from other functions. This is a powerful feature that enables functional programming patterns.

### Assigning Functions to Variables

Functions can be stored in variables just like any other value:
```python
def greet(name):
    return f"Hello, {name}!"

say_hello = greet  # Assign function to variable
result = say_hello("Alice")
# Result: "Hello, Alice!"
```

### Passing Functions as Arguments

You can pass functions as parameters to other functions:
```python
def apply_operation(x, y, operation):
    return operation(x, y)

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

result1 = apply_operation(5, 3, add)       # Result: 8
result2 = apply_operation(5, 3, multiply)  # Result: 15
```

### Returning Functions from Functions

Functions can return other functions:
```python
def create_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))  # Result: 10
print(triple(5))  # Result: 15
```

### Using Built-in Higher-Order Functions

Python provides functions that work with functions as objects:

**map()** — Apply a function to all items in an iterable:
```python
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
result = list(map(square, numbers))
# Result: [1, 4, 9, 16, 25]
```

**filter()** — Filter items based on a function that returns True/False:
```python
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(is_even, numbers))
# Result: [2, 4, 6]
```

**sorted()** with key parameter — Sort using a custom function:
```python
words = ["apple", "pie", "banana", "kiwi"]
result = sorted(words, key=len)
# Result: ["pie", "apple", "kiwi", "banana"]
```

### Lambda Functions

Lambda functions are small anonymous functions useful for simple operations:
```python
# Instead of defining a full function
def add(a, b):
    return a + b

# You can use a lambda
add = lambda a, b: a + b

# Commonly used with map, filter, and sorted
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
# Result: [1, 4, 9, 16, 25]
```

---

## Testing and Debugging in Python

Testing ensures your code works correctly, while debugging helps you find and fix errors when something goes wrong.

### Debugging with print()

The simplest debugging method is using `print()` statements to see what's happening:
```python
def calculate_average(numbers):
    print(f"Input: {numbers}")
    total = sum(numbers)
    print(f"Total: {total}")
    average = total / len(numbers)
    print(f"Average: {average}")
    return average

result = calculate_average([10, 20, 30])
```

### Using the debugger (pdb)

Python's built-in debugger lets you step through code line by line:
```python
import pdb

def calculate_average(numbers):
    pdb.set_trace()  # Execution pauses here
    total = sum(numbers)
    average = total / len(numbers)
    return average
```

When you run this, you can use commands like `n` (next), `s` (step), `c` (continue), and `p variable_name` (print).

### Unit Testing with unittest

Write formal tests to verify your functions work correctly:
```python
import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)
    
    def test_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)
    
    def test_zero(self):
        self.assertEqual(add(0, 5), 5)

if __name__ == "__main__":
    unittest.main()
```

### Using pytest

pytest is a popular testing framework that's simpler than unittest:
```python
def multiply(a, b):
    return a * b

def test_multiply_positive():
    assert multiply(3, 4) == 12

def test_multiply_negative():
    assert multiply(-2, 3) == -6

def test_multiply_zero():
    assert multiply(0, 100) == 0
```

Run tests with `pytest filename.py` in your terminal.

### Assertions

Use assertions to check that conditions are true during development:
```python
def divide(a, b):
    assert b != 0, "Divisor cannot be zero"
    return a / b

result = divide(10, 0)  # Raises AssertionError with message
```

### Type Checking with isinstance()

Catch type-related bugs early by validating input types:
```python
def process_data(data):
    if not isinstance(data, list):
        raise TypeError("data must be a list")
    
    return [x * 2 for x in data if isinstance(x, (int, float))]

# This raises TypeError immediately
process_data("not a list")
```

### Try-Except Blocks

Handle errors gracefully:
```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    except TypeError:
        print("Error: Both values must be numbers")
        return None

print(safe_divide(10, 0))   # Error: Cannot divide by zero
print(safe_divide(10, "x")) # Error: Both values must be numbers
```

### Logging

Use the logging module for more detailed debugging information:
```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def calculate(x, y):
    logger.debug(f"Calculating with x={x}, y={y}")
    result = x + y
    logger.info(f"Result: {result}")
    return result

calculate(5, 3)
```

### Best Practices

Write defensive code that validates inputs and provides clear error messages. Combine multiple debugging techniques: use print statements for quick checks, unit tests to ensure correctness, and the debugger when you're stuck on a complex issue. Always test edge cases (empty lists, zero values, None, negative numbers) and write tests as you develop, not after.
