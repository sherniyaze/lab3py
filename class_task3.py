# Define a class named Rectangle which inherits 
# from Shape class from task 2. Class instance 
# can be constructed by a length and width. The 
# Rectangle class has a method which can compute 
# the area.


class Shape():
    def __init__(self):
        self.length = 0
        self.width = 0
    def areas(self):
        return 0

class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        self.lengthy = int(input())
        self.widthy = int(input())
    def areas(self):
        return self.lengthy*self.widthy

my_fav_rectangle = Rectangle()
print(my_fav_rectangle.areas())