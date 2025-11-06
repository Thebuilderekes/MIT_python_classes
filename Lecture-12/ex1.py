def do_this(my_list):
    l_copy = [e for e in list(my_list)]
    ## code doesn't need to be this bulky just an example of list comprehension in use
    breakpoint()
    result = [print(f"{e} is an employee") for e in l_copy]
    return result


this_list = ["magaret", "johnny", "Tamuno"]
do_this(this_list)


