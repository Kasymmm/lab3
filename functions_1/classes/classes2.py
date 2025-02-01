#Define a class named Shape and its subclass Square. 
#The Square class has an init function which takes a length as argument.
#Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

class Shape():
    def _init_(self):
        pass

    def Area(self):
        return 0;

class Square(Shape):
    def _init_(self, length):
        super()._init_()
        self.length = length

    def area(self):
        return self.length ** 2

shape = Shape()
i = int(input())
square = Square(i)
print(square.area)