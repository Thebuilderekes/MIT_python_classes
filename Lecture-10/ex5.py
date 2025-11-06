"""function to mutate list given to it"""


def square_list(my_list):
    """function to mutate list given to it"""
    for i, elem in enumerate(my_list):
        my_list[i] = elem**2
    return my_list

print(square_list([1,2,3,4,5]))
