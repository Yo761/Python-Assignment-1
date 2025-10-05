# Task 1: Perform Basic Mathematical Operations

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Performing mathematical operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handling division carefully to avoid ZeroDivisionError
if num2 != 0:
    division = num1 / num2
else:
    division = "undefined (cannot divide by zero)"

# Displaying the results
print("\nResults:")
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
