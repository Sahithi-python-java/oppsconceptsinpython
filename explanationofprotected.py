'''Main Uses of the Protected Access Modifier in Real Programming
1. Internal API Design (Encapsulation)
Protected access modifiers are useful when you want to create a clear boundary between internal logic and 
external use of the class. You want to signal to other developers (or even to yourself) that certain methods
 or attributes should only be modified or accessed within the class or by subclasses.

For example, in a complex system, you might expose public methods to interact with the class but hide
 protected methods that contain business logic or internal calculations. By using the protected modifier, 
 you reduce the risk of someone using these methods incorrectly.'''

## Example:

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number  # Public attribute
        self._balance = balance               # Protected attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount           # Accessing protected attribute internally
        else:
            raise ValueError("Deposit amount must be positive")

    def _calculate_interest(self):            # Protected method
        # Internal method to calculate interest, not intended for external use
        return self._balance * 0.05

    def apply_interest(self):
        # Public method that uses the protected method internally
        self._balance += self._calculate_interest()

# Public usage of the class
account = BankAccount("12345", 1000)
account.deposit(200)
print(account._balance)  # You could access it, but you're discouraged from doing so


'''2. Inheritance and Subclasses
Protected members make sense when you expect a class to be extended or inherited. They allow subclasses to
 access and reuse the internal logic of the parent class without exposing that logic to external code. 
 This gives flexibility to the subclass, while still keeping certain logic hidden from the outside world.

For example, a framework might provide base classes with protected members that are not intended to be 
accessed directly by users of the framework but can be used by developers extending the framework with 
new features.'''

## example:

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary                 # Protected attribute

    def get_salary(self):
        return self._salary

    def _calculate_bonus(self):               # Protected method
        return self._salary * 0.10            # Logic for bonus calculation

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_bonus(self):
        # Subclass can access protected method from parent class
        return self._calculate_bonus() * self.team_size

manager = Manager("Alice", 70000, 5)
print(manager.get_bonus())  # Works fine as subclass accesses protected method

'''Here, _calculate_bonus() is a protected method in the parent class Employee, accessible only within 
the Manager subclass. This ensures that the bonus logic is hidden from external users while allowing 
subclasses to customize behavior.'''

'''3. Guidelines for Large Teams
When working in large teams or on large projects, using the protected access modifier provides a clear 
indication of how your code is structured. If every attribute or method were public, the internal logic 
of a class could easily be misused or altered in unintended ways. The use of the _ convention helps 
document the internal workings of a class, making it easier for new developers to understand what 
parts of the code should not be modified directly.

In this way, protected members function as internal documentation that enhances code readability
 and maintainability.

4. Framework and Library Design
Protected members are often used in frameworks and libraries where certain parts of the code are intended
 to be extensible or customizable, but other parts should not be directly manipulated. When you're building 
 reusable components, it’s important to define what parts of the class can be modified by users of the 
 library and what parts should remain untouched.

For example, you might provide a base class with some protected methods that can be reused and extended, but
 should not be used directly in the application code.'''

## Example: 

class BaseView:
    def render(self):
        # Public method to render the view
        return self._build_content()

    def _build_content(self):
        # Protected method to be used or overridden in subclasses
        return "Default Content"

class CustomView(BaseView):
    def _build_content(self):
        # Override the protected method to customize behavior
        return "Customized Content"

view = CustomView()
print(view.render())  # Output: Customized Content

'''In this case, _build_content() is a protected method meant to be overridden by subclasses, 
while render() is a public method that uses the protected method internally. External users of the CustomView 
class don’t need to know about _build_content().'''

'''5. Enforcing Encapsulation and Flexibility
The protected modifier lets you enforce encapsulation while also providing flexibility. You encapsulate 
internal logic that should not be exposed, but still allow controlled access in specific situations 
(like inheritance). This is a middle ground between public and private access, giving you a way to
 communicate intent.

In contrast, private members (using __) are meant for complete encapsulation, where even subclasses aren't 
allowed to access them directly.'''

### To Summarize:
'''Protected members aren’t just for name’s sake; they serve an important purpose in signaling how attributes 
and methods should be used.
They help enforce encapsulation while still allowing inheritance and customization within subclasses.
In large-scale projects, they provide clarity for teams on what should and shouldn't be accessed or modified
directly.
They are essential in the design of frameworks and libraries where part of the internal logic is shared,
but only within a controlled environment.

By using protected members, you get to balance flexibility (allowing subclasses to inherit and override
 behavior) and encapsulation (keeping the internal logic hidden from direct external access).'''
