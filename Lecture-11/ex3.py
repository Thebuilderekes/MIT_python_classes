"""
Showing the difference between deep copy and shallow copy
"""


import copy

my_list = [1,2, [34,5], 6, 7]
new_list = copy.copy(my_list)  # which is the equivalent pf new_list = my_list[:]
my_list.append([100])

my_list[0] = 50  #modifies only top level which is not shared
my_list[2][0] = 42 # modifies nested mutable list which is shared
my_list.append("in my list") #modifies only top level which is not shared
print(my_list)

print(new_list)

# Important caveat: Since this is a shallow copy, my_list and new_list
# share references to the nested lists.
# This means: Modifying nested elements in either list will affect both
# But appending to the top level only affects the list you're modifying
# The code demonstrates a common pitfall: using copy.copy() (shallow copy) on a nested structure,
# which might not give you the independent copy you expect!

# Using deepcopy
##new_list = copy.deepcopy(my_list)
#with deepcopy you get back a true copy of my_list that does not allow the for
# modification at both the top and nested list level

