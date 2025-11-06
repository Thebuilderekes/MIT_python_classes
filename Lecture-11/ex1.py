"""
modules to show how to remove a give element from a list
"""

def remove_all(my_list, e):
    """
    Removes all occurrences of element 'e' from the list 'my_list' in-place.
    """
    filtered_list = []

    for item in my_list:
        if item != e:
            filtered_list.append(item)
    my_list.clear()
    my_list.extend(filtered_list)


# Example Usage:
my_data = [1, 2, 3, 4, 2, 5, 2]
print(f"Original list: {my_data}")

remove_all(my_data, 2)
print(f"List after removing 2: {my_data}") # Output: [1, 3, 4, 5]

remove_all(my_data, 4)
print(f"List after removing 4: {my_data}") # Output: [1, 3, 5]
