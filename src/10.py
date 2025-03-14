import random
from typing import List
def get_random_code(n: int) -> List[int]:
    """Returns a list of n random numbers between 1 and 6"""
    return [random.randint(1, 6) for _ in range(n)]