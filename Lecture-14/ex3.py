def check_dict_list_for_num(my_list , num):
    """checking if a number exists in a list of dictionaries"""
    for list_dict in my_list:
        if num in list_dict:
            return True
    return False

d1 ={2:4, 3:8, 1:4}
d2 ={4:4, 6:8, 7:4}
d3 ={8:4, 1:8, 3:4}

d = [d1, d2, d3]

result =check_dict_list_for_num(d, 8)
print(result)
