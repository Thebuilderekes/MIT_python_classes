# Python Dictionaries: Complete Guide

## What is a Dictionary?

~/.config

A dictionary is an unordered collection of key-value pairs. Unlike lists which use numeric indices, dictionaries use unique keys to access values.
Dictionaries are mutable, meaning you can add, remove, or modify items after creation.

### Basic Syntax

Dictionaries are created using curly braces `{}` with key-value pairs separated by colons:

```python
# Empty dictionary
empty_dict = {}

# Dictionary with initial data
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

# Keys and values can be of different types
mixed = {
    "string_key": "value",
    1: "numeric key",
    (1, 2): "tuple key"
}
```

### Key Requirements

Keys must be immutable and hashable (meaning they can't be changed). Valid key types include strings, numbers, tuples, and booleans. Lists and dictionaries cannot be keys because they are mutable.

```python
# Valid keys
valid = {
    "name": "Bob",
    42: "answer",
    (1, 2): "tuple",
    True: "boolean"
}

# Invalid: Lists cannot be keys
invalid = {
    [1, 2]: "this will error"  # TypeError: unhashable type
}
```


## Creating and Initializing Dictionaries

### Literal Syntax

```python
person = {"name": "John", "age": 30, "city": "New York"}
```

### dict() Constructor

```python
# From list of tuples
person = dict([("name", "John"), ("age", 30)])

# From keyword arguments
person = dict(name="John", age=30, city="New York")

# From another dictionary
copy = dict(person)
```

### Dictionary Comprehension

Create dictionaries using a comprehension similar to list comprehensions:

```python
# Create a dictionary of squares
squares = {x: x**2 for x in range(5)}
# Result: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Create from lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
result = {k: v for k, v in zip(keys, values)}
# Result: {"a": 1, "b": 2, "c": 3}

# With conditions
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
# Result: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```


## Accessing Dictionary Values

### Using Keys

Access values by putting the key in square brackets:

```python
student = {"name": "Alice", "age": 20, "grade": "A"}

print(student["name"])   # Alice
print(student["age"])    # 20
```

### get() Method

The `get()` method is safer because it returns `None` if the key doesn't exist, rather than raising an error:

```python
student = {"name": "Alice", "age": 20}

print(student.get("name"))        # Alice
print(student.get("email"))       # None
print(student.get("email", "N/A")) # N/A (default value)
```

### Checking if a Key Exists

Use the `in` operator to check membership:

```python
student = {"name": "Alice", "age": 20}

if "name" in student:
    print(student["name"])  # Alice

if "email" not in student:
    print("Email not found")
```


## Adding and Modifying Items

### Adding New Items

```python
student = {"name": "Alice", "age": 20}

# Add a new key-value pair
student["email"] = "alice@example.com"
student["grade"] = "A"

# Result: {"name": "Alice", "age": 20, "email": "alice@example.com", "grade": "A"}
```

### Modifying Existing Items

```python
student = {"name": "Alice", "age": 20}

# Modify existing value
student["age"] = 21
student["name"] = "Alicia"

# Result: {"name": "Alicia", "age": 21}
```

### update() Method

Update multiple items at once:

```python
student = {"name": "Alice", "age": 20}

# Add/modify multiple items
student.update({"age": 21, "grade": "A", "city": "Boston"})

# Result: {"name": "Alice", "age": 21, "grade": "A", "city": "Boston"}
```

### setdefault() Method

Set a value only if the key doesn't exist:

```python
student = {"name": "Alice"}

# Key exists, so it's not changed
student.setdefault("name", "Bob")      # Returns "Alice"

# Key doesn't exist, so it's added
student.setdefault("age", 20)          # Returns 20 and adds it

# Result: {"name": "Alice", "age": 20}
```


## Removing Items

### del Statement

```python
student = {"name": "Alice", "age": 20, "grade": "A"}

del student["grade"]

# Result: {"name": "Alice", "age": 20}
```

### pop() Method

Remove an item and return its value:

```python
student = {"name": "Alice", "age": 20, "grade": "A"}

grade = student.pop("grade")        # Returns "A"
email = student.pop("email", "N/A") # Returns "N/A" (default if not found)

# Result: {"name": "Alice", "age": 20}
```

### popitem() Method

Remove and return an arbitrary key-value pair:

```python
student = {"name": "Alice", "age": 20}

key, value = student.popitem()  # Removes last inserted item
# Result: student = {"name": "Alice"} and key, value = ("age", 20)
```

### clear() Method

Remove all items from a dictionary:

```python
student = {"name": "Alice", "age": 20}

student.clear()

# Result: {}
```


## Iterating Through Dictionaries

### Iterating Over Keys

```python
student = {"name": "Alice", "age": 20, "grade": "A"}

for key in student:
    print(key)  # Prints: name, age, grade
```

### Iterating Over Values

```python
for value in student.values():
    print(value)  # Prints: Alice, 20, A
```

### Iterating Over Key-Value Pairs

```python
# Using items()
for key, value in student.items():
    print(f"{key}: {value}")
    # Prints:
    # name: Alice
    # age: 20
    # grade: A

# Using keys() explicitly (less common)
for key in student.keys():
    print(f"{key}: {student[key]}")
```


## Dictionary Methods

### keys(), values(), items()

Return view objects containing dictionary keys, values, or key-value pairs:

```python
student = {"name": "Alice", "age": 20, "grade": "A"}

keys = student.keys()       # dict_keys(['name', 'age', 'grade'])
values = student.values()   # dict_values(['Alice', 20, 'A'])
items = student.items()     # dict_items([('name', 'Alice'), ('age', 20), ('grade', 'A')]) # notice the type of dict_items. You can use .item()to iterate over the key-value pairs in a list

list(keys)## can be cast to a list
list(values)## can be cast to a list
list(items)## can be cast to a list

# Convert to lists if needed
keys_list = list(keys)      # ['name', 'age', 'grade']
```

### copy()

Create a shallow copy of a dictionary:

```python
student = {"name": "Alice", "age": 20}

copy = student.copy()

# Modify the copy without affecting original
copy["age"] = 21

print(student)  # {"name": "Alice", "age": 20}
print(copy)     # {"name": "Alice", "age": 21}
```

### fromkeys()

Create a dictionary with specified keys and a default value:

```python
keys = ["name", "age", "grade"]

# All values default to None
result = dict.fromkeys(keys)
# Result: {"name": None, "age": None, "grade": None}

# All values default to "N/A"
result = dict.fromkeys(keys, "N/A")
# Result: {"name": "N/A", "age": "N/A", "grade": "N/A"}
```


## Nested Dictionaries

Dictionaries can contain other dictionaries:

```python
company = {
    "employee1": {
        "name": "Alice",
        "age": 30,
        "department": "Engineering"
    },
    "employee2": {
        "name": "Bob",
        "age": 28,
        "department": "Sales"
    }
}

# Access nested values
print(company["employee1"]["name"])  # Alice
print(company["employee2"]["age"])   # 28
```

### Iterating Through Nested Dictionaries

```python
for emp_id, emp_data in company.items():
    print(f"{emp_id}: {emp_data['name']} works in {emp_data['department']}")
    # Prints:
    # employee1: Alice works in Engineering
    # employee2: Bob works in Sales
```


## Merging Dictionaries

### Using update()

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

dict1.update(dict2)

print(dict1)  # {"a": 1, "b": 2, "c": 3, "d": 4}
```

### Using the Merge Operator (Python 3.9+)

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

result = dict1 | dict2  # Creates a new dictionary

print(result)   # {"a": 1, "b": 2, "c": 3, "d": 4}
print(dict1)    # {"a": 1, "b": 2} (unchanged)
```

### Using Dictionary Comprehension

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

result = {**dict1, **dict2}

print(result)  # {"a": 1, "b": 2, "c": 3, "d": 4}
```


## Common Patterns and Use Cases

### Counting Occurrences

```python
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)  # {"apple": 3, "banana": 2, "cherry": 1}

# Or using dictionary comprehension
word_count = {word: words.count(word) for word in set(words)}
```

### Default Values with defaultdict

```python
from collections import defaultdict

# Using get() method
word_count = {}
for word in ["apple", "banana", "apple"]:
    word_count[word] = word_count.get(word, 0) + 1

# Or using defaultdict (cleaner)
word_count = defaultdict(int)
for word in ["apple", "banana", "apple"]:
    word_count[word] += 1  # No need for get(), defaults to 0
```

### Grouping Data

```python
students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"},
    {"name": "Charlie", "grade": "A"},
    {"name": "Diana", "grade": "B"}
]

# Group by grade
by_grade = {}
for student in students:
    grade = student["grade"]
    if grade not in by_grade:
        by_grade[grade] = []
    by_grade[grade].append(student["name"])

print(by_grade)
# Result: {"A": ["Alice", "Charlie"], "B": ["Bob", "Diana"]}
```

### Using Dictionaries with JSON

```python
import json

# Convert dictionary to JSON string
student = {"name": "Alice", "age": 20, "grade": "A"}
json_string = json.dumps(student)
print(json_string)  # {"name": "Alice", "age": 20, "grade": "A"}

# Convert JSON string to dictionary
data = json.loads(json_string)
print(data["name"])  # Alice
```


## Dictionary vs Other Data Structures

| Structure | Ordered | Indexed | Mutable | Use Case |
|-----------|---------|---------|---------|----------|
| List | Yes | Yes (numeric) | Yes | Ordered collection of items |
| Tuple | Yes | Yes (numeric) | No | Fixed collection of items |
| Dictionary | Yes (Python 3.7+) | Yes (by key) | Yes | Key-value associations |
| Set | No | No | Yes | Unique items, membership testing |

---

## Performance Considerations

Dictionary lookups are very fast (O(1) average time complexity) because they use hash tables internally. This makes dictionaries ideal for searching and accessing data by key, even with millions of items.

```python
# Fast lookup
large_dict = {f"key{i}": i for i in range(1000000)}
value = large_dict["key500000"]  # Very fast, constant time
```

---

## Best Practices

Use descriptive key names for clarity. When working with nested dictionaries, consider using the `get()` method or try-except blocks to handle missing keys gracefully. Use type hints to document what your dictionaries should contain. For large datasets with many keys, consider using classes or dataclasses instead of deeply nested dictionaries. Always validate and sanitize dictionary keys when they come from user input. Use dictionary comprehensions for clean, Pythonic code when creating dictionaries from other data structures.
