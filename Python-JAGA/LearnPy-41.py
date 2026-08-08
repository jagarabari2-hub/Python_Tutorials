print()
print("|========================================|"
      "| Inheritance In Python "
      "||========================================|")
print()
class Base:
    def __init__(self):
        self.name = "JAGA RABARI"
    def display(self):
        print("Name:", self.name)
class Derived(Base):
    def disp(self):
        print("This is the derived class")
obj = Derived()
obj.display()
obj.disp()
print()
print("|========================================|"
      "| Single Inheritance "
      "||========================================|")
print()
class Base1:
    def __init__(self):
        self.name = "JAGA RABARI"
    def display(self):
        print("Name:", self.name)
class Derived1(Base1):
    def disp(self):
        print("Derived method of Base1")
class Base2:
    def __init__(self):
        self.name = "JAGA RABARI"
    def show(self):
        print("Name:", self.name)
class Derived2(Base2):
    def showMessage(self):
        print("Derived method of Base2")
obj1 = Derived1()
obj2 = Derived2()
obj1.display()
obj1.disp()
obj2.show()
obj2.showMessage()
print()
print("|========================================|"
      "| Multilevel Inheritance "
      "||========================================|")
print()
class Base:
    def __init__(self):
        self.name = "JAGA RABARI"
    def display(self):
        print("Name:", self.name)
class Derived1(Base):
    def disp(self):
        print("Derived1 method of Base")


class Derived2(Derived1):
    def showMessage(self):
        print("Derived2 method of Derived1")
obj = Derived2()
obj.display()
obj.disp()
obj.showMessage()
print()
print("|========================================|"
      "| Hierarchical Inheritance "
      "||========================================|")
print()
class Base:
    def __init__(self):
        self.name = "JAGA RABARI"
    def display(self):
        print("Name:", self.name)
class Derived1(Base):
    def disp(self):
        print("My base class is Base")

class Derived2(Base):
    def showMessage(self):
        print("My base class is Base")
class Derived3(Derived1):
    def showMessage(self):
        print("My base class is Derived1")
class Derived4(Derived1):
    def dispMsg(self):
        print("My base class is Derived1")
o1 = Derived4()
o2 = Derived3()
o3 = Derived2()
o1.display()
o1.disp()
o1.dispMsg()
o2.name="JAGA RABARI"
o2.display()
o2.disp()
o2.showMessage()
o3.name="JAGA RABARI"
o3.display()
o3.showMessage()
print()
print("|========================================|"
      "| Multiple Inheritance "
      "||========================================|")
print()
class Base1:
    def __init__(self, p, q):
        self.p = p
        self.q = q
        p = int(input("Enter value of p: "))
        q = int(input("Enter value of q: "))
        j = p + q
        print("The value of p and q are:", p, q)
        print("Sum:", j)
class Base2:
    def __init__(self, r, s):
        self.r = r
        self.s = s
        r = int(input("Enter value of r: "))
        s = int(input("Enter value of s: "))
        k = r * s
        print("The value of r and s are:", r, s)
        print("Product:", k)
class Derived(Base1, Base2):
    def __init__(self, p, q, r, s):
        Base1.__init__(self, p, q)
        Base2.__init__(self, r, s)
obj = Derived(0, 0, 0, 0)
print()
print("|========================================|"
      "| Multiple Inheritance, Finding Circles Area "
      "||========================================|")
print()
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
class Cylinder:
    def __init__(self, height):
        self.height = height
    def volume(self, radius):
        return 3.14 * radius * radius * self.height
class CircleCylinder(Circle, Cylinder):
    def __init__(self, radius, height):
        Circle.__init__(self, radius)
        Cylinder.__init__(self, height)
radius = float(input("Enter the radius of the circle: "))
height = float(input("Enter the height of the cylinder: "))
circle_cylinder = CircleCylinder(radius, height)
print("Area of the circle:", circle_cylinder.area())
print("Volume of the cylinder:", circle_cylinder.volume(radius))
print()
print("|========================================|"
      "| Method Overriding "
      "||========================================|")
print()
class Base:
    def show(self):
        print("This is the base class")
    def disp(self):
        print("Winter is coming")
class Derived(Base):
    def show(self):
        print("This is the derived class")
    def disp(self):
        print("Summer is coming")
obj = Derived()
obj.show()
obj.disp()
print()
print("|========================================|"
      "| Using constructor in derived class only "
      "||========================================|")
print()
class Base:
    def __init__(self):
        self.s = "Constructor in derived class"
    def show(self):
        print("Name:", self.s)
class Derived(Base):
    def disp(self):
        print("Chaos is a ladder")
obj = Derived()
obj.show()
obj.disp()
print()
print("|========================================|"
      "| Using constructor in both class "
      "||========================================|")
print()
class Base:
    def __init__(self):
        self.s = "Incursion is on multiverse"
    def show(self):
        print("Incursion is on multiverse")
class Derived(Base):
    def __init__(self):
        self.n = "Chaos is a ladder"
    def disp(self):
        
        print(self.n)
obj = Derived()
obj.disp()
obj.show()
print()
print("|========================================|"
      "| Method Resolution Order (MRO) "
      "||========================================|")
print()
class A:
    pass
class B:
    pass
class C:
    pass
class D(A, B):
    pass
class E(B, C):
    pass
class F(D, E, C):
    pass
print(F.mro())                                                                         