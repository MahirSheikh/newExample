# Calculator class
class Calculator:
    def __init__(self, value):
        self.value = value

    def power(self, n):
        return self.value ** n

    def add(self, n):
        return self.value + n

    def subtract(self, n):
        return self.value - n

    def multiply(self, n):
        return self.value * n

    def divide(self, n):
        return self.value / n

    def remainder(self, n):
        return self.value % n


# Main program
calculator = Calculator(2)
print(calculator.power(3))
print(calculator.add(3))
print(calculator.subtract(3))
