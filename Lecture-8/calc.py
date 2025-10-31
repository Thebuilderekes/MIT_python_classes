def calc(op, x, y):
    return op(x, y)


def div(a, b):
    if b != 0:
        return a / b
    print("denom is 0")


res = calc(div, 2, 0)


print(res)
