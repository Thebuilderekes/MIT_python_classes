"""Using sachecking for criteria"""


def apply(criteria, n):
    """check if criteria for the number of numbers needed to add from 0 to n"""
    count = 0
    for i in range(0, n + 1):
        if criteria(i):
            count += 1
    return f"this is count: {count}"


def is_even(n):
    """check if n is even"""
    return n % 2 == 0


HOW_MANY = apply(is_even, 12)

print(HOW_MANY)
