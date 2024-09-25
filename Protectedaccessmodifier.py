class Animal:
    def __init__(self, name, age):
        self.name = name      # Public attribute
        self._age = age       # Protected attribute (single underscore)
    
    def _speak(self):         # Protected method
        return f"{self.name} makes a sound."

    def get_info(self):
        return f"Name: {self.name}, Age: {self._age}"

# Subclass of Animal
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def dog_info(self):
        return f"Breed: {self.breed}, Age: {self._age}"  # Accessing protected attribute

    def make_sound(self):
        return self._speak()  # Accessing protected method


# Create an object of the Dog class
dog = Dog("Buddy", 5, "Golden Retriever")

# Accessing public method
print(dog.get_info())  # Output: Name: Buddy, Age: 5

# Accessing protected attribute directly (discouraged but possible)
print(dog._age)  # Output: 5

# Calling protected method (discouraged but possible)
print(dog._speak())  # Output: Buddy makes a sound.


'''In Python, the concept of access modifiers is more relaxed than in languages like Java or C++. Python uses naming conventions rather than strict access control to suggest the intended visibility of variables and methods. The protected access modifier is part of this convention, and it’s represented using a single underscore (_).

What Is a Protected Access Modifier?
In Python, protected members (attributes or methods) are intended to be accessible within the class and its subclasses, but not from outside the class.
Protected members are not strictly private, and Python doesn’t enforce access restrictions. However, by convention, you should not access protected members outside the class hierarchy.
How to Define Protected Members:
A protected attribute or method is indicated by prefixing its name with a single underscore (_).'''

'''Key Points:
Protected Attribute (_age):

It’s prefixed with a single underscore _, indicating it should be treated as a protected member.
Accessible in Subclasses: The subclass Dog can access _age without any issues because it’s a protected member.
Not Strictly Enforced: You can still access _age from outside the class (e.g., dog._age), but it's discouraged.
Protected Method (_speak):

The method _speak is marked as protected and is intended to be used within the class and its subclasses only.
The Dog subclass calls _speak() without any problems, as it’s meant to be accessible in subclasses.
Direct Access (Discouraged):

Although the convention tells developers not to access protected members directly (e.g., dog._age or dog._speak()), Python does not strictly prevent this.
Accessing protected members outside the class hierarchy is considered bad practice, even though it is technically allowed.
Why Use Protected Members?
Encapsulation: Helps in encapsulating data, meaning you are restricting access to internal variables and methods, but still allowing subclasses to use them.
Code Organization: Protected members are useful when you want to share some internal logic with subclasses but don’t want them to be exposed to external code.
Difference Between Protected and Public:
Public members are freely accessible from outside the class and are not prefixed by underscores.
Protected members are accessible within the class and its subclasses and are marked with a single underscore (_).
Private members (for reference) are marked with a double underscore (__) and are name-mangled to prevent direct access from outside the class.
Conclusion:
In Python, protected members are indicated by a single underscore (_) and are meant to be accessed only within the class and its subclasses.
Python doesn’t enforce access restrictions like other languages, but it uses conventions to indicate intent.
Even though protected members can technically be accessed from outside the class, it's considered bad practice to do so.'''