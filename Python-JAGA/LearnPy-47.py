print()
print("|========================================|"
      "| Exercise 1 "
      "||========================================|")
print()
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def movingSpeed(self):
        pass
class Car(Vehicle):
    def movingSpeed(self):
        speed = 60
        print(f"The moving speed of the car is {speed} km/h.")

class Bus(Vehicle):
    def movingSpeed(self):
        speed = 40
        print(f"The moving speed of the bus is {speed} km/h.")

# Create objects of the derived classes
car = Car()
bus = Bus()

# Call the abstract method
car.movingSpeed()
bus.movingSpeed()
print()
print("|========================================|"
      "| Exercise 2 "
      "||========================================|")
print()
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("The dog barks.")
class Cat(Animal):
    def sound(self):
        print("The cat meows.")
# Create objects of the derived classes
dog = Dog()
cat = Cat()
# Call the abstract method
dog.sound()
cat.sound()
