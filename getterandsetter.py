class Person:
    def __init__(self, name, age):
        self.name = name
        # Private attribute (by convention, underscore is used for private variables)
        self._age = age
    
    # Getter method for age
    def get_age(self):
        return self._age
    
    # Setter method for age (with validation)
    def set_age(self, age):
        if age > 0:
            self._age = age
        else:
            print("Age can't be negative or zero!")

# Creating an object of Person class
person = Person("Sahithi", 25)

# Accessing age using getter
print(person.get_age())  # Output: 25

# Updating age using setter
person.set_age(30)       # Age is updated to 30 # Age is first set to 30
print(person.get_age())  # Output: 30 # Once the age is set, and then age is  

# Trying to set an invalid age
person.set_age(-5)       # Output: Age can't be negative or zero!

'''In Python (and other object-oriented languages), getter and setter methods are used to access and update private attributes of a class.
They provide controlled access to class attributes, ensuring encapsulation and data integrity.

What is Encapsulation?
Encapsulation is one of the core principles of OOP, where the internal state of an object (its attributes) is hidden from outside interference and access. Instead of accessing or modifying attributes directly, you use methods (getters and setters) to interact with them.

Getter and Setter Methods:
Getter Method: A method that allows you to retrieve the value of a private attribute.
Setter Method: A method that allows you to set or update the value of a private attribute, with optional validation or conditions.
Why Use Getters and Setters?
To protect private variables from being modified directly.
To add validation or control over how attributes are accessed or modified.
To make future changes easier without affecting the rest of your code.'''
