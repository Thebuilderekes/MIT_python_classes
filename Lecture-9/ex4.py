def check_even(fn, n):
    for i in range(n):
        if fn(i):
            print(f"{i} is even")
        elif not fn(i):
            print(f"{i} is not even")


def is_even(n):
    return n % 2 == 0


print(check_even(is_even, 10))
