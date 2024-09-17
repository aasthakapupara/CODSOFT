# CODSOFT/Python programming internship/Task 2/CALCULATOR

import math

# Define arithmetic functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def modulus(x, y):
    if y != 0:
        return x % y
    else:
        return "Error! Division by zero."

def exponent(x, y):
    return x ** y

def root(x, y):
    if x >= 0:
        return x ** (1 / y)
    else:
        return "Error! Negative number cannot be used for root."

def calculator():
    print("\n-------Simple Calculator-------\n")
    
    # Input: First number
    num1 = float(input("Enter the first number: "))
    
    # Input: Second number
    num2 = float(input("Enter the second number: "))
    
    # Input: Operation choice
    print("\nChoose an operation:\n")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponent")
    
    choice = input("\nEnter the number corresponding to the operation (1/2/3/4/5/6): ")
    
    if choice == '1':
        result = add(num1, num2)
        print(f"\nThe result of {num1} + {num2} is: {result}\n")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"\nThe result of {num1} - {num2} is: {result}\n")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"\nThe result of {num1} * {num2} is: {result}\n")
    elif choice == '4':
        result = divide(num1, num2)
        print(f"\nThe result of {num1} / {num2} is: {result}\n")
    elif choice == '5':
        result = modulus(num1, num2)
        print(f"\nThe result of {num1} % {num2} is: {result}\n")
    elif choice == '6':
        result = exponent(num1, num2)
        print(f"\nThe result of {num1} ** {num2} is: {result}\n")
    else:
        print("\nInvalid input! Please enter a number between 1 and 6.\n")

# Run the calculator
calculator()
