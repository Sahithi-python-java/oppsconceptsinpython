# Base class
class Father:
    def outputf(self):
        print("I am Father")

# Derived class
class Mother(Father):
    def outputm(self):
        print("I am Mother")

# Child class inheriting from Mother (which inherits from Father)
class Child(Mother):
    def outputc(self):
        print("I am Child")

# Creating object of Child
c = Child()

# Access methods from Father, Mother, and Child
c.outputf()  # I am Father
c.outputm()  # I am Mother
c.outputc()  # I am Child

# Check MRO
print(Child.mro()) ##'''This will give output as [<class '__main__.Child'>, <class '__main__.Mother'>, <class '__main__.Father'>, <class 'object'>]
'''

##Learning Points for Your Notes:
##Multiple Inheritance: In Python, a class can inherit from multiple classes, but make sure to avoid 
redundant inheritance.
Method Resolution Order (MRO): Python uses MRO to determine the order in which parent classes are checked
 for methods. Use ClassName.mro() to inspect it.
Avoid Redundant Inheritance: If one parent class already inherits from another, it’s usually unnecessary
 to have a child class inherit from both.
Simplifying Code: Simplify the class hierarchy when possible to make the relationships between classes
 easier to understand and maintain.
 
 The MRO will now be much simpler and more intuitive. The Child class will look for methods in:
Child
Mother
Father
object (the root class in Python)
Verifying MRO:
To check the Method Resolution Order (MRO) in this simpler example, you can use the mro() method:

'''