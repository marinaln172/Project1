import numpy as np

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

n = int(input("Enter a number: "))
print(f"The factorial of {n} is: {calculate_factorial(n)}")
