print()
print("|========================================|"
      "| Abstract Class "
      "||========================================|")
print()
from abc import ABC, abstractmethod
class AbcBaseClass(ABC):
    def __init__(self):
        print("Abstract Class")
    @abstractmethod
    def abMeth(self):
        pass
    def conMeth(self):
        print("I'm a concrete method")
class Derived(AbcBaseClass):
    def abMeth(self):
        print("I'm redefined")
o = Derived()
o.abMeth()
o.conMeth()
print()
print("|========================================|"
      "| An Abstract Method "
      "||========================================|")
print()
class AbsBaseClass(ABC):
    def __init__(self):
        print("Abstract class")
    
    @abstractmethod
    def abMeth(self):
        print("I provide the basic functionality that can be enriched by my subclass")
    
    def conMeth(self):
        print("I'm a concrete method")
class Derived(AbsBaseClass):
    def abMeth(self):
        super().abMeth()
        print("I'm redefined")
o = Derived()
o.abMeth()
o.conMeth()