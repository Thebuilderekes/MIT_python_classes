def create_tuple(*args):
    for i in args:
        print(i)
    return args


my_tuple = create_tuple(2)
print(type(my_tuple))
