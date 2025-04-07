import numpy as np

def add_numbers(a, b):
    """
    Add two numbers and return the result.
    
    Args:
        a (int or float): The first number.
        b (int or float): The second number.
        
    Returns:
        int or float: The sum of a and b.
    """
    return a + b

def calculate_square_root(number):
    """
    Calculate the square root of a given number.
    
    Args:
        number (float): The number to calculate the square root of.
        
    Returns:
        float: The square root of the given number.
    """
    return np.sqrt(number)

def main():
    # Example usage
    num1 = 4.5
    result_add_numbers = add_numbers(num1, 3)
    print("Result of adding 3 to", num1, "is:", result_add_numbers)
    
    square_root_result = calculate_square_root(9)
    print("Square root of 9 is:", square_root_result)

if __name__ == "__main__":
    main()
