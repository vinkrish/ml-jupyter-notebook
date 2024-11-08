#  Function Arguments and Return Types
def add(x: int, y: int) -> int:
    return x + y

result = add(3, 5)
print(result)  # Output: 8

# Variable Annotations
name: str = "Alice"
age: int = 30
is_student: bool = False

# Type Hinting with Complex Data Types
from typing import List, Tuple, Dict

# List of integers
numbers: List[int] = [1, 2, 3]

# Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 30)

# Dictionary with string keys and integer values
scores: Dict[str, int] = {"math": 90, "science": 85}

# Type Hinting with Optional Values (Optional)
from typing import Optional

def greet(name: Optional[str] = None) -> str:
    if name is None:
        return "Hello, Guest!"
    return f"Hello, {name}!"

print(greet())           # Output: Hello, Guest!
print(greet("Alice"))    # Output: Hello, Alice!

# Type Hinting with Union
from typing import Union

def process_data(data: Union[int, str]) -> str:
    if isinstance(data, int):
        return f"Number: {data}"
    elif isinstance(data, str):
        return f"Text: {data}"

print(process_data(100))     # Output: Number: 100
print(process_data("Hello")) # Output: Text: Hello

# Type Hinting with Any
from typing import Any

def print_value(value: Any) -> None:
    print(value)

print_value(123)       # Output: 123
print_value("Hello")   # Output: Hello
print_value([1, 2, 3]) # Output: [1, 2, 3]

# Type Hinting with Callable
from typing import Callable

def apply_function(x: int, func: Callable[[int], int]) -> int:
    return func(x)

result = apply_function(5, lambda x: x * 2)
print(result)  # Output: 10

# Type Hinting with Classes (Self Type)
from typing import Self

class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

    def set_next(self, node: Self) -> Self:
        self.next = node
        return self

# Example usage
node1 = Node(1)
node2 = Node(2)
node1.set_next(node2)
