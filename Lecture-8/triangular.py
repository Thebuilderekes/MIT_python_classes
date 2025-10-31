"""module to check if argument is triangular"""


def triangular(n):
    """check if n is triangular"""
    total = 0
    for i in range(n+1):
        total += i
        print(total)
        if total == n:
            return True
    return False


##123456
print("is n triangular?", triangular(1))
