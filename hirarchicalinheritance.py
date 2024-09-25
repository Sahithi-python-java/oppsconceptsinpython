class Parent():
    def outputp(self):
        print("I am Parent")
class Child1(Parent):
    def outputc1(self):
        print("I am Child1")
class Child2(Parent):
    def outputc2(self):
        print("I am Child2")

c1=Child1()
c2=Child2()

c1.outputp()
c1.outputc1()
c2.outputp()
c2.outputc2()


## Please do compcare both the programs for better understanding for return type and print

class Parent():
    def outputp(self):
        return "I am Parent"  # Return instead of print

class Child1(Parent):
    def outputc1(self):
        return "I am Child1"  # Return instead of print

class Child2(Parent):
    def outputc2(self):
        return "I am Child2"  # Return instead of print

# Creating objects for Child1 and Child2
c1 = Child1()
c2 = Child2()

# Now using print to print the returned values
print(c1.outputp())   # Output: I am Parent
print(c1.outputc1())  # Output: I am Child1
print(c2.outputp())   # Output: I am Parent
print(c2.outputc2())  # Output: I am Child2


## Each method now returns a string rather than printing it directly.
## You can then use print() to display the returned value when calling the method.
## Multiple child classes inherit from the same parent class.
