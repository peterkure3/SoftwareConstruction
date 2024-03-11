import math

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def sin(self, angle):
        return math.sin(angle)

    def cos(self, angle):
        return math.cos(angle)

    def tan(self, angle):
        return math.tan(angle)

    def sqrt(self, num):
        return math.sqrt(num)

    def cbrt(self, num):
        return num**(1/3)