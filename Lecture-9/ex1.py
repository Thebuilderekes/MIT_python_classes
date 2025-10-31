"""
Using a higher order function apply checking for criteria
with different conditions using lambda functions
"""


## so when apply is called, criteria gets passed the lambda function as an argument and i gets tested based on it
def apply(criteria, n):
    """check if criteria for the number of numbers needed to add from 0 to n"""
    count = 0
    for i in range(0, n + 1):
        if criteria(i):
            count += 1
    return f"this is count: {count}"


###lambda function used to directly define a function and return based on condition
HOW_MANY = apply(lambda n: n % 2 == 0, 12)

print(HOW_MANY)
