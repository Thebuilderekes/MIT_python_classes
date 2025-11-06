"""
module to find a number that matches a number in the list and removes it"""
def remove_all(my_list, e):
    for i in my_list:
        if i == e:
            my_list.remove(i)

    return my_list


## There is an issue with remove because it is mutation the original array during iteration so it will miss a 2 if it is used in [1,2,2,2]
## loop index stays while the first 2 spotted is removed, making the
#second 2 take it's space, on the second loop, it skips that 2   and goes on to remove
# the next 2 and it will keep missing 2's if the 2's are adjacent


## to solve this issue you will have to create a copy and iterate over that and remove from the original while doing so


#my_list = my_list[:] to make a copy

result = remove_all([1,2,2,2], 2)
print(result)

