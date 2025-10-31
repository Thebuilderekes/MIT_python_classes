# slicing in reverse with index that exceeds what is available
name = "abrakadabra"

# print(len(name))
# print(name[len(name) : : -1])
# In the case above, it does not have and index that is the len(name)
# which is 11, slicing is forgiving and assumes that you meant to start at the very last character
# it will start in reverse and include every character since it was to provided a stop index

print(name[2])

# slicing in a direction that has the stop index less than the start
# print(name[5: 2])
# Python tries to go forward from index 5 to get to index 2. Since index 5 is already past index 2, it's impossible to move forward to reach it.

# Because the slice conditions can't be met, Python doesn't raise an error; it just returns an empty string: ''
