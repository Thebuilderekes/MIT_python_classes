"""module displaying class and inheritance"""
class Animal():
    def __init__(self, age):
        self.age =age
    def __str__(self):
        return "This animal is " + str(self.age) + " years old"

## when doing an operation like this one where you are setting
#dictionary keys to a class Object value,you will have to expose the
#class object by lopping over it

def create_dict(L):
    d ={}
    for item in L:
        if isinstance(item, int):
            d[item] = Animal(item)
    return d

result =create_dict([2,'a', 5, 6, 'jane'])
for k, v in result.items():
    print(f"{k}: {v} ")
