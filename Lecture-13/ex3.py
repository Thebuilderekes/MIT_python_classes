def pairwise_div(Ldom, Lnum):
    pair = []
    for i, item in enumerate(list(Ldom)):
        pass
    for i, num in enumerate(list(Lnum)):
        try:
            new_num = Ldom[i]/Lnum[i]
            pair.append(new_num)

        except ZeroDivisionError as e:
            print(f"{e}")

    return pair


list_one = [40, 15, 20]
list_two = [20, 3, 10]
result = pairwise_div(list_one, list_two)
print(result)
