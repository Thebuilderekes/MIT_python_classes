# pylint: disable=C0114
class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age



    def __str__(self):
        return f"Animal name: {self.name} age: {self.age}"


def make_animal(list2, list1):
    animal_list = []
#creates a list of animals with the same length as L1 and L2
#An animal object at index i has age and name corresponding to
# index as L1 and L2 respectively

    for i, _ in enumerate(list1):
        animal_item = Animal(list2[i], list1[i])
        animal_list.append(animal_item)

    return animal_list


L1= [2,4,6,7]
L2 =["fox", "cow", "fish", "goat"]

result = make_animal(L2, L1)
for item in result:
    print(item)



class Person(Animal):
    def __init__(self, name: str, age: int, talk: str) -> None:
        super().__init__(name, age)  # Call parent class constructor
        self.talk: str = talk

    def say_something(self, sentence) -> str:
        self.talk = sentence
        return self.talk




# Subclass that inherits from Animal
class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str, is_trained: bool) -> None:
        super().__init__(name, age)  # Call parent class constructor
        self.breed: str = breed
        self.is_trained: bool = is_trained

    def get_breed(self) -> str:
        return self.breed

    def set_breed(self, breed: str) -> None:
        self.breed = breed

    def is_dog_trained(self) -> bool:
        return self.is_trained

    def train_dog(self) -> None:
        self.is_trained = True

    def bark(self) -> str:
        return f"{self.name} says: Woof! Woof!"

    def __str__(self) -> str:
        # Override parent __str__ to include new attributes
        return f"name: {self.name} age: {self.age} breed: {self.breed} trained: {self.is_trained}"


# Example usage
if __name__ == "__main__":


    jane =Person("Jane", 34, "hello")
    judy=Person("judy", 84, "hello")
    # Create a Dog instance
    bull_dog = Dog("Buddy", 3, "Bull dog", False)
    golden_dog = Dog("pookey", 3, "Golden Retriever", False)


    def make_pets():
        person_list =[jane, judy]
        dog_list =[bull_dog, golden_dog]
        d ={person.get_name(): dog.get_name() for person, dog in zip(person_list, dog_list)}
        return d

    a  = {}
    result= make_pets()
    print(result)



