def multiply_numbers(a: int, b: int) -> int:
    """
    This function takes two integers as input and returns their product.
    
    Example usage:
    >>> multiply_numbers(2, 3)
    6
    
    >>> multiply_numbers(-4, 5)
    -20
    """
    return a * b

# Test the function with provided data points
assert multiply_numbers(2, 3) == 6
assert multiply_numbers(-4, 5) == -20
