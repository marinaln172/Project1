
import random

def generate_random_python_code():
    # Generate a random number between 1 and 10
    num = random.randint(1, 10)

    # Generate a random string
    word = "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for i in range(5))

    # Return the code
    return f"print('The number is {num} and the string is {word}')"