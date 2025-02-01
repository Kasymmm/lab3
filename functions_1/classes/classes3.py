#Define a class named Rectangle which inherits from Shape class from task 2.
#Class instance can be constructed by a length and width.
#The Rectangle class has a method which can compute the area.

class Shape():
    def _init_(self):
        pass

    def area(self):
        return 0;

class Square(Shape):
    def _init_(self, length):
        super()._init_()
        self.length = length

    def area(self):
        return self.length ** 2

class Rectangles(Shape):
    def _init_(self, length, width):
        super()._init_()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    

shape = Shape()
a = int(input())
b = int(input())
rectangle = Rectangles(a, b)
print("Area of Rectangle:", rectangle.area())