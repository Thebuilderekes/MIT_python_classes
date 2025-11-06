def sum_prod(l):
    product = 1
    nsum = 0
    for i in l:
        product = product * i
        nsum = nsum + i
    return (nsum, product)


result = sum_prod([2, 3, 4])

print(result)
