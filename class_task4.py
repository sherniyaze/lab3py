import math
class Point:
    def __init__(self):
        self.position_by_X = int(input())
        self.position_by_Y = int(input())
    def show(self):
        print("Coordinates of our point:", self.position_by_X, ";", self.position_by_Y)
    
    def move(self):
        self.position_by_X = int(input())
        self.position_by_Y = int(input())
        print(f"New coordinates> x:{self.position_by_X}, y:{self.position_by_Y}")
    
    def distance(self, new_point):
        return math.sqrt((new_point.position_by_X - self.position_by_X)**2 + (new_point.position_by_Y - self.position_by_Y)**2)
my_fav_point = Point()
my_fav_point.show()
my_fav_point.move()
my_FAVORY_point = Point()
distance = my_fav_point.distance(my_FAVORY_point)
print(distance)