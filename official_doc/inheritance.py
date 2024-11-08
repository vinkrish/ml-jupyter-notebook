# Single Inheritance: One class inherits from another.
# Base class (Parent)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal."

# Derived class (Child)
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Example usage
dog = Dog("Buddy")
print(dog.speak())  # Output: Buddy says Woof!

# Multiple Inheritance: A class inherits from more than one class.
# Base class 1
class Flyer:
    def fly(self):
        return "I can fly!"

# Base class 2
class Swimmer:
    def swim(self):
        return "I can swim!"

# Derived class
class Duck(Flyer, Swimmer):
    def quack(self):
        return "Quack!"

# Example usage
duck = Duck()
print(duck.fly())    # Output: I can fly!
print(duck.swim())   # Output: I can swim!
print(duck.quack())  # Output: Quack!

# Multilevel Inheritance: A class inherits from a derived class.
# Base class
class Vehicle:
    def info(self):
        return "This is a vehicle."

# Derived class
class Car(Vehicle):
    def wheels(self):
        return "This vehicle has 4 wheels."

# Derived class from Car
class ElectricCar(Car):
    def battery(self):
        return "This car has a battery."

# Example usage
tesla = ElectricCar()
print(tesla.info())   # Output: This is a vehicle.
print(tesla.wheels()) # Output: This vehicle has 4 wheels.
print(tesla.battery())# Output: This car has a battery.

# Hierarchical Inheritance: Multiple classes inherit from a single base class.
# Base class
class Shape:
    def __init__(self, color):
        self.color = color

# Derived class 1
class Circle(Shape):
    def draw(self):
        return f"Drawing a {self.color} circle."

# Derived class 2
class Square(Shape):
    def draw(self):
        return f"Drawing a {self.color} square."

# Example usage
circle = Circle("red")
square = Square("blue")

print(circle.draw())  # Output: Drawing a red circle.
print(square.draw())  # Output: Drawing a blue square.

# Hybrid Inheritance: A mix of different inheritance types.
# Base class
class Engine:
    def start(self):
        return "Engine started."

# Derived class 1
class Car(Engine):
    def drive(self):
        return "Car is driving."

# Derived class 2
class Boat(Engine):
    def sail(self):
        return "Boat is sailing."

# Derived class from both Car and Boat
class AmphibiousVehicle(Car, Boat):
    def info(self):
        return "This vehicle can drive on land and sail on water."

# Example usage
amphibious_vehicle = AmphibiousVehicle()
print(amphibious_vehicle.start())  # Output: Engine started.
print(amphibious_vehicle.drive())  # Output: Car is driving.
print(amphibious_vehicle.sail())   # Output: Boat is sailing.
print(amphibious_vehicle.info())   # Output: This vehicle can drive on land and sail on water.

# Explicitly call Parent Class Constructor
# Parent class
class Person:
    def __init__(self, name, age):
        print("Calling Parent Constructor")
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(Name: {self.name}, Age: {self.age})"

# Child class
class Employee(Person):
    def __init__(self, name, age, employee_id):
        # Calling the parent class constructor using super()
        super().__init__(name, age)
        print("Calling Child Constructor")
        self.employee_id = employee_id
        
    def __str__(self):
        # Using the parent class's __str__ method and extending it
        return f"{super().__str__()}, Employee ID: {self.employee_id}"

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}")

# Example usage
emp = Employee("Alice", 30, "E123")
emp.display()
