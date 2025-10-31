"""
This module provides functions to sum all odd or even numbers between two integers.
"""


def check_odd(i):
    """check if argument is an odd number"""
    return i % 2 != 0


def check_even(i):
    """check if argument is an even number"""
    return i % 2 == 0


def sum_num(a, b):
    """sum all odd numbers between a and b"""
    sum_of_odds = 0
    for i in range(a, b + 1):
        if check_odd(i):
            print(f"{i} is odd")
            sum_of_odds += i
    return sum_of_odds


print("The sum of odd number between a nd b are: ", sum_num(2, 7))
