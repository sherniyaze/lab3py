# Define a class named Shape and its subclass
# Square. The Square class has an init function
# which takes a length as argument. Both classes
# have a area function which can print the area
# of the shape where Shape's area is 0 by default.

class Shape:
    def __init__(self):
        self.lengthy = 0
        self.widthy = 0
    def area(self):
        return 0

class Square(Shape):
    def __init__(self):
        super().__init__()
        self.lengthy = int(input())
    def area(self):
        return self.lengthy**2


my_square = Square()
print(my_square.area())
