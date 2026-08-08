print()
print("|========================================|"
      "| An Abstract Method "
      "||========================================|")
print()
from abc import ABC, abstractmethod
class AbsBaseClass(ABC):
    def __init__(self):
        print("Guess the number game in python with class and abstract method")
    
    @abstractmethod
    def numGuess(self):
        pass
class Derived(AbsBaseClass):
    def numGuess(self):
        import random
        num = random.randint(1, 10)
        guess = int(input("Guess a number between 1 and 10: "))
        if guess == num:
            print("Congratulations! You guessed the number.")
        else:                          
            print(f"Sorry, the correct number was {num}.")  
o = Derived()
o.numGuess()
print()
print("|========================================|"
      "| An Interfaces "
      "||========================================|")
print()
class interface(ABC):
    @abstractmethod
    def method1(self):
        pass
    @abstractmethod
    def method2(self):
        pass
    @abstractmethod
    def method3(self):
        pass
class Derived(interface):
    def method1(self):
        print("I am redefined method1")
    def method2(self):
        print("I am redefined method2")
    def method3(self):
        print("I am redefined method3")

o = Derived()
o.method1()
o.method2()
o.method3()