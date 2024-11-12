class DefaultConstructorExample:
    def __init__(self):
        # This is a default constructor
        self.message = "Hello, World!"

    def display_message(self):
        print(self.message)

# Creating an instance
obj = DefaultConstructorExample()
obj.display_message()  # Output: Hello, World!

class ParameterizedConstructorExample:
    def __init__(self, name, age):
        # This is a parameterized constructor
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def __str__(self):
        # User-friendly string representation
        # return f"ParameterizedConstructorExample(Name: {self.name!r}, Age: {self.age})"
        return f"ParameterizedConstructorExample(Name: {self.name}, Age: {self.age})"

    def __repr__(self):
        # Unambiguous string representation
        # return f"<ParameterizedConstructorExample('{self.name}', {self.age})>"
        return f"ParameterizedConstructorExample(name='{self.name}', age={self.age})"

# Creating an instance with parameters
obj2 = ParameterizedConstructorExample("Alice", 30)
obj2.display_info()  # Output: Name: Alice, Age: 30

# Using __str__ method (via print)
print(obj)  # Output: ParameterizedConstructorExample(Name: Alice, Age: 30)

# Using __repr__ method
print(repr(obj))  # Output: ParameterizedConstructorExample(name='Alice', age=30)

class ClassMethodConstructorExample:
    # class attribute
    alive = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, info_str):
        # Alternative constructor that takes a single string argument
        name, age = info_str.split(", ")
        return cls(name, int(age))
    
    def died(self):
        ClassMethodConstructorExample.alive = False

    def instance_died(self):
        self.alive = False # this is instance attribute, shadowing the class attribute

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating an instance using the class method
obj3 = ClassMethodConstructorExample.from_string("Bob, 25")
obj3.display_info()  # Output: Name: Bob, Age: 25

class StaticMethodConstructorExample:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def is_adult(age):
        # A static method to check if someone is an adult
        return age >= 18

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Using the static method
print(StaticMethodConstructorExample.is_adult(20))  # Output: True
print(StaticMethodConstructorExample.is_adult(15))  # Output: False

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Class method constructor
    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = 2024 - birth_year
        return cls(name, age)

    # Static method
    @staticmethod
    def is_adult(age):
        return age >= 18

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Using the main constructor
person1 = Person("Alice", 30)
person1.display_info()  # Output: Name: Alice, Age: 30

# Using the class method constructor
person2 = Person.from_birth_year("Bob", 1995)
person2.display_info()  # Output: Name: Bob, Age: 29

# Using the static method
print(Person.is_adult(17))  # Output: False
print(Person.is_adult(18))  # Output: True
