print("|========================================|"
      "| Method Overloading "
      "||========================================|")
print()
class A:
    def add(self, a, b):
        print("Addition of " + str(a) + " and " + str(b) + " is: " + str(a + b))
    def add(self, a, b, c):
        print("Addition of " + str(a) + ", " + str(b) + ", and " + str(c) + " is: " + str(a + b + c))
class B:
    def sub(self, a, b):
        print("Subtraction of " + str(a) + " and " + str(b) + " is: " + str(a - b))
    def sub(self, a, b, c):
        print("Subtraction of " + str(a) + ", " + str(b) + ", and " + str(c) + " is: " + str(a - b - c))
A().add(int(input("Enter first number: ")), int(input("Enter second number: ")), int(input("Enter third number: ")))
B().sub(int(input("Enter first number: ")), int(input("Enter second number: ")), int(input("Enter third number: ")))
print()
class A:
    def display(self, a = "Hello World"):
        print(a)
A().display()
A().display("Welcome to Python")
print()
print("|========================================|"
      "| Duck Typing "
      "||========================================|")
print()
class A:
    def calculate(self, a, b):
        return a + b
print(A().calculate(10, 20))
print(A().calculate("JAGA ", "RABARI"))
print(A().calculate(3.14, 2.71))
print()
print("|========================================|"
      "| Resolving Method Overriding "
      "||========================================|")
print()
class A:
    def __init__(self):
        self.s = "THIS IS CLASS A"
    def method(self):
        print(self.s)
class B(A):
    def method(self):
        super().method()
        print("THIS IS CLASS B")
B().method()
print()
class C:
    def __init__(self):
        self.s = "THIS IS CLASS C"
    def method(self):
        print(self.s)
class D(C):
    def method(self):
        C.method(self)
        print("THIS IS CLASS D")
D().method()
print()
