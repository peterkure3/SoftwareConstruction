import math

class Calculator:
    def add(self, a, b):
        """Add two numbers."""
        return a + b

    def subtract(self, a, b):
        """Subtract two numbers."""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b

    def divide(self, a, b):
        """Divide two numbers."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def sin(self, angle):
        """Calculate the sine of an angle."""
        return math.sin(angle)

    def cos(self, angle):
        """Calculate the cosine of an angle."""
        return math.cos(angle)

    def tan(self, angle):
        """Calculate the tangent of an angle."""
        return math.tan(angle)

    def sqrt(self, num):
        """Calculate the square root of a number."""
        return math.sqrt(num)

    def cbrt(self, num):
        """Calculate the cube root of a number."""
        return num**(1/3)