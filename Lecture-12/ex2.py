"""module showing uses of list comprehension to build array using loop"""
num = [len(x) for x in ["xy", 6 , "go", "4.0"] if isinstance(x, str )]



print(num)
