# Basic Calculator
print("Welcome to the Basic Calculator!")

# Input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter an operation (+, -, *, /): ")

# Perform calculation
if operation == "+":
    result = num1 + num2
    print(f"The result of {num1} + {num2} is {result}")
elif operation == "-":
    result = num1 - num2
    print(f"The result of {num1} - {num2} is {result}")
elif operation == "*":
    result = num1 * num2
    print(f"The result of {num1} * {num2} is {result}")
elif operation == "/" and num2 != 0:
    result = num1 / num2
    print(f"The result of {num1} / {num2} is {result}")
else:
    print("Invalid operation or error.")
