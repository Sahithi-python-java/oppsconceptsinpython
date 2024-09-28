# Demonstrating Data Encapsulation in Python

class Employee:
    def __init__(self, name, salary):
        # Private variables (Encapsulation)
        # These variables are intended to be accessed only within the class
        self.__name = name  # Name is private
        self.__salary = salary  # Salary is private

    # Public method to access private variable __name
    def get_name(self):
        return self.__name  # Getter for name

    # Public method to modify private variable __name
    def set_name(self, name):
        self.__name = name  # Setter for name

    # Public method to access private variable __salary
    def get_salary(self):
        return self.__salary  # Getter for salary

    # Public method to modify private variable __salary
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary  # Setter for salary with validation
        else:
            print("Invalid salary!")  # Salary can't be negative

# Creating an object of Employee class
emp = Employee("John", 50000)

# Accessing private variables using getter methods
print(emp.get_name())  # Output: John
print(emp.get_salary())  # Output: 50000

# Trying to modify private variables using setter methods
emp.set_name("Jane")
emp.set_salary(60000)

# Accessing the updated values
print(emp.get_name())  # Output: Jane
print(emp.get_salary())  # Output: 60000

# Trying to set an invalid salary
emp.set_salary(-100)  # Output: Invalid salary!


## Encapsulation: Hiding data (variables) inside the class and restricting direct access from outside the 
# class.
## Private Variables: Variables prefixed with __ to indicate they are private and should not be accessed 
## directly.
## Getter and Setter Methods: Public methods used to access and modify private variables.