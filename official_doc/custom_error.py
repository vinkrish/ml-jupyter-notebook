# Basic Custom Error Class
class CustomError(Exception):
    """A custom exception for demonstration purposes."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Example usage
try:
    raise CustomError("This is a custom error message!")
except CustomError as e:
    print(f"Error occurred: {e}")

# Custom Error Class with Additional Attributes
class ValidationError(Exception):
    """Exception raised for validation errors."""
    def __init__(self, message, field, value):
        self.message = message
        self.field = field
        self.value = value
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}. Field: {self.field}, Value: {self.value}"

# Example usage
try:
    raise ValidationError("Invalid value", "age", -1)
except ValidationError as e:
    print(e)

# Using Custom Error Classes with Inheritance
class ApplicationError(Exception):
    """Base class for all application-specific errors."""
    pass

class DatabaseError(ApplicationError):
    """Exception raised for database errors."""
    def __init__(self, message):
        super().__init__(message)

class NetworkError(ApplicationError):
    """Exception raised for network-related errors."""
    def __init__(self, message):
        super().__init__(message)

# Example usage
try:
    raise DatabaseError("Database connection failed.")
except ApplicationError as e:
    print(f"Application error: {e}")

# Custom Error Class with Logging
import logging

class FileError(Exception):
    """Exception raised for file-related errors."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        logging.error(self.message)

# Configure logging
logging.basicConfig(level=logging.ERROR)

# Example usage
try:
    raise FileError("Failed to open file: data.txt")
except FileError as e:
    print(f"Handled error: {e}")
