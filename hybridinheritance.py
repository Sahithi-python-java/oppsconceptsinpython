# Base class
class Animal:
    def sound(self):
        return "Animal Sound"

# Intermediate class 1
class Mammal(Animal):
    def has_hair(self):
        return True

# Intermediate class 2
class Pet:
    def pet_type(self):
        return "Domestic Animal"

# Derived class inheriting from both Mammal and Pet
class Dog(Mammal, Pet):
    def bark(self):
        return "Woof!"

# Example usage
dog = Dog()
print(dog.sound())     # Output: Animal Sound
print(dog.has_hair())  # Output: True
print(dog.pet_type())  # Output: Domestic Animal
print(dog.bark())      # Output: Woof!


## A combination of two or more types of inheritance. It can involve multiple and multilevel inheritance.