"""example to show how objects in memory are handled but in the case of lists
"""

def handle_list(my_list):
    for e in my_list:
        my_list = my_list + my_list
        # if this was `my_list.extend(my_list)` it would cause the 
        # list to grow infinitely on each loop, causing never ending iteration 
        #than leads to an infinite loop
        print(my_list)

handle_list([2,3])
