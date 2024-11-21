import math
from functions.error_handler import ConvertNumberType

class Calculator:
    def Save(self, value):
        with open('History.txt', 'a') as file:
            file.write(f"{value}\n")

    def Add(self, a, b):
        result = a + b
        self.Save(f"{a} + {b} = {result}")
        return result

    def Subtract(self, a, b):
        result = a - b
        self.Save(f"{a} - {b} = {result}")
        return result

    def Multiply(self, a, b):
        result = a * b
        self.Save(f"{a} * {b} = {result}")
        return result

    def Divide(self, a, b):
        if b != 0:
            result = a / b
            self.Save(f"{a} / {b} = {result}")
            return result
        else:
            raise ValueError("Division by zero is not allowed")

    def Mod(self, a, b):
        result = a % b
        self.Save(f"{a} % {b} = {result}")
        return result

    def SquareRoot(self, number):
        result = math.sqrt(number)
        self.Save(f"Square root of {number} = {result}")
        return result

    def Exponentiate(self, a, b):
        result = a ** b
        self.Save(f"{a}^{b} = {result}")
        return result

    def GetHistory(self):
        with open("History.txt", "r") as file:
            return file.read()
