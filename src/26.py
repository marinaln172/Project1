import random

def roll_dice():
    """
    Simulate rolling a 6-sided die.
    Returns:
        int: The result of rolling the die.
    """
    return random.randint(1, 6)

print(roll_dice())
