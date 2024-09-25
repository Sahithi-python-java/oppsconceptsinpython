class PrivateExample:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age  # Private attribute

    def __display_info(self):  # Private method
        return f"Name: {self.__name}, Age: {self.__age}"

    def get_info(self):  # Public method to access private method
        return self.__display_info()

obj = PrivateExample("Sahithi", 32)

# Direct access will result in an error
# print(obj.__name)  # AttributeError

# Accessing via a public method
print(obj.get_info())  # Output -> Name: Sahithi, Age: 32
