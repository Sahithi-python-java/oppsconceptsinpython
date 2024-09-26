## Example of Polymorphism
class Duck:
    def quack(self):
        return "Quack!"

class Dog:
    def bark(self):
        return "Woof!"

class Person:
    def quack(self):
        return "I'm pretending to be a duck!"

def make_it_quack(thing):
    print(thing.quack())

# Creating instances of classes
duck = Duck()
person = Person()
dog = Dog()

# The duck and the person can "quack"
make_it_quack(duck)    # Output: Quack!
make_it_quack(person)  # Output: I'm pretending to be a duck!

# The dog cannot "quack" (will raise an error if called)
# make_it_quack(dog)   # Uncommenting this line will raise an AttributeError