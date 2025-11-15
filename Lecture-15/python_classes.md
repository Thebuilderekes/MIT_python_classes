## Python class
Classes are a way in python that allows us to define our own custom objects with behaviours that we define for them.

Object we design are going instances of a data type.

When we design objects we consider these 2 aspects:
- An internal representation
- An interface for interacting with the object


## Defining a python class

```
class ClassName(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y

```

Where the `self` keyword is what allows the data to persist through the life cycle of the class object

Every variable attached to the `self` will persist through out the life cycle of the object

## Creating a p

