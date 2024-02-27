class Calculator:
    
    def add(self, a, b):
        # Addition operation
        return a + b

    def subtract(self, a, b):
        # Subtraction operation
        return a - b

    def multiply(self, a, b):
        # Multiplication operation
        return a * b

    def divide(self, a, b):
        # Division operation with a check for division by zero
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
