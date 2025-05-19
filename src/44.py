import random

def generate_random_string(length):
    """
    Generate a random string of given length.
    """
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(random.choice(characters) for _ in range(length))

# Example usage:
random_string = generate_random_string(10)
print(random_string)
