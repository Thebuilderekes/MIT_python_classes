"""dividing elements in both list arguments"""



def pairwise_div(l_dom, l_num):
    """dividing elements in both list arguments"""

    my_list =[]
    for i, _ in enumerate(l_num):
        try:
            new_list= l_dom[i]/l_num[i]
            my_list.append(new_list)
        except ZeroDivisionError as e:
            print(f"cannot allow {e}")
            return f"cannot divide {l_dom[i]} by {l_num[i]}"
    return my_list


list_one = [40, 15, 20]
list_two = [20, 3,  20]
result = pairwise_div(list_one, list_two)
print(result)
