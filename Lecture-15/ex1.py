class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        """calculate area of rectangle"""
        return self.width* self.height


    def get_width(self):
        """return width"""
        return self.width

    def get_height(self):
        """return height"""
        return self.height

    def __str__(self):
        return "This rectangle has a width of " \
                + str(self.width) +" and a height of " + str(self.height)

one_rectangle= Rectangle(2, 5)
#print("this is width", one_rectangle.width)
#result = one_rectangle.calculate_area()

print(one_rectangle)
