
def addition(a, b):
    return a + b


def subtraction(a, b):
    return abs(a - b)


def product(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "Error: Division by zero not allowed"
    return a / b


# Input
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Output
print("Addition:", addition(a, b))
print("Subtraction (positive):", subtraction(a, b))
print("Multiplication:", product(a, b))
print("Division:", division(a, b))
