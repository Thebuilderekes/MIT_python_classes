def apply(criteria, n):
    """check if criteria for the number of numbers needed to add from 0 to n"""
    return criteria(n)


def add_up(n):
    """add up numbers form 0 to n"""
    total = 0
    count = 0
    for i in range(0, n + 1):
        total += i
        count += 1
        if total == n:
            print("criteria satisfied")
            print(f"it took {count} numbers adding from 0 to {n} to add up to {n} ")
            return True


print(apply(add_up, 6))
