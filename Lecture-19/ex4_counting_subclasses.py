# pylint: disable=C0114
class Animal():
# I can use a tag variable to keep track of the number of objects that are going to made from this
    #class by setting it and incrementing in in the __init__function
    tag = 1
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.aid = Animal.tag
        Animal.tag += 1


    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def get_aid(self):
        return str(self.aid).zfill(5)  #zfill adds zeros, in this case 5 Zeros
                                        #to the number to make it id like

    def __str__(self):
        return f"Animal name: {self.name} age: {self.age}"


dog1 = Animal("dogie", 2)
dog2 = Animal("dogie", 2)
print(dog1.get_aid())
print(dog2.get_aid())
