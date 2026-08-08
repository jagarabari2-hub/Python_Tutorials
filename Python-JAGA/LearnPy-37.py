print()
print("|========================================|"
      "| OOP Concept Classses and Objects "
      "||========================================|")
print()
# Illustration of Object in Python
r = 2
l = ['1', '2']
d = {'Name':'Sam'}
def myfun():
    x = 222
print(type(myfun()))
print(type(r))
print(type(l))
x = print(type(d))
print(type(x))
print()
print("|========================================|"
      "| Class Data Members and Methods "
      "||========================================|")
print()
class MyFirstClass:
    my_first_string = "This is my first class"
    def show(self):
        print(self.my_first_string)
obj = MyFirstClass()
obj.show()
obj.my_first_string = input("Enter String\n")
obj.show()
print()
print("|========================================|"
      "| Constructor and Destructor "
      "||========================================|")
print()
class MyClass:
    def __init__(self,q,p):
        self.q = q
        self.p = p
    def disp(self):
        return self.q,self.p
o1 = MyClass(input("Enter String 1:\n"), int(input("Enter Number 1:\n")))
o2 = MyClass(input("Enter String 2:\n"), int(input("Enter Number 2:\n")))
print(o1.disp())
print(o2.disp())
print("|========================================|"
      "| Illustration of a Destructor "
      "||========================================|")
print()
class MyClass:
    def __init__(self,q,p):
        self.q = q
        self.p = p
    def disp(self):
        return self.q,self.p
    def __del__(self):
        print("Destroyed")

o1 = MyClass(input("Enter String 1:\n"), int(input("Enter Number 1:\n")))
o2 = MyClass(input("Enter String 2:\n"), int(input("Enter Number 2:\n")))
print(o1.disp())
print(o2.disp())
# del(o1)
print(o1.disp())
print("|========================================|"
      "| Class and instance variable "
      "||========================================|")
print()
class MyClass:
    c_variable = "I'm shared by all instances "
    def __init__(self,q,p):
        self.q = q        
        self.p = p

o = MyClass(125648, 4144444156)
print(o.q, o.p)
print(MyClass.c_variable)        
print()
# Counting the number of instance of a class
class MyClass:
    count = 0
    def __init__(self):
        MyClass.count+=1
o1 = MyClass()
o1 = MyClass()
o1 = MyClass()
o1 = MyClass()
o1 = MyClass()
o1 = MyClass()
o1 = MyClass()
o1 = MyClass()
o1 = MyClass()
print("No. of instance created :",MyClass.count)
print()
print("|========================================|"
      "| Instance, class and static methods "
      "||========================================|")
print()
# Illustration of Different kinds of methods
class MyClass:
    def iMethod(sel):
        print("Instance method", sel)
    @classmethod
    def cMethod(c):
        print("Class Method", c)
    @staticmethod
    def sMethod():
        print("Static method")
o = MyClass()
o.iMethod()
MyClass.cMethod()
o.cMethod()
MyClass.sMethod()
o.sMethod()
print()
print("|========================================|"
      "| Illustration of Methods and attribute "
      "||========================================|")
print()
class MyClass:
    """This is a document string"""
    def __init__(self):
        self.name = "JAGA RABARI"
# Note that MyClass() is an object
print(getattr(MyClass(), "name"))
print(hasattr(MyClass(), "name"))
print(hasattr(MyClass(), "age"))
print(isinstance(MyClass(), MyClass))
print(dir(MyClass()))
print(MyClass() .__doc__)
print(MyClass() .__module__)
print(MyClass() .__dict__)
print()
print("|========================================|"
      "| Illustration of Access Modifiers "
      "||========================================|")
print()
class MyClass:
    def publicMethod(s):
        return "Public Method"
    def _ProtectedMethod(s):
        return "Single-underscore method"
    def __privateMethod(s):
        return "Double-underscore method"
obj = MyClass()
print(obj.publicMethod())
print(obj._ProtectedMethod())
print(obj._MyClass__privateMethod())
