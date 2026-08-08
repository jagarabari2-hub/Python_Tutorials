print()
print("|========================================|"
      "| Operator Overriding "
      "||========================================|")
print()
class myclass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, o):
        temp = myclass(self.a + o.a, self.b + o.b)
        temp.a = self.a + o.a
        temp.b = self.b + o.b
        return temp


obj1 = myclass(10, 20)
obj2 = myclass(30, 40)
obj3 = obj1 + obj2
print("obj1.a = ", obj1.a, " obj1.b = ", obj1.b)
print("obj2.a = ", obj2.a, " obj2.b = ", obj2.b)
print("After adding obj1 and obj2 :")
print("obj3.a = ", obj3.a, " obj3.b = ", obj3.b)