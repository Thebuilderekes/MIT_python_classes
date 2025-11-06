"""creates list from 0 to n inclusive"""


def create_list(n):
    """creates list from 0 to n inclusive"""
    my_list = []
    for i in range(0, n + 1):
        # the 0 in the range is option as it
        # will default to 0 if you don't add it
        my_list.append(i)
    return my_list


print(create_list(5))
