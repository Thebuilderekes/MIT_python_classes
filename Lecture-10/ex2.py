def remove_elem(my_list, e):
    """creating a list from an input list that is absent of the 
    second argument
    """
    new_list = []
    for i in my_list:
        if i != e:
            new_list.append(i)
    return new_list


print(remove_elem([1,2,3,4,5,6], 2))
