print("Write a program consisting of a single class, `Shape`, which defines a method, `area()`. Overload the method area() to return the area of the shapes, triangle and rectangle, one at a time.")
print()
class Shape:
    def area(self, a, b):
        return a * b
    def area(self, a, b, c):
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5 
shape = Shape()
print("Area of rectangle: " + str(shape.area(5, 10)))
print("Area of triangle: " + str(shape.area(3, 4, 5)))