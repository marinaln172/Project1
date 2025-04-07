import random
def add_random_number():
    random_numbers = [random.randint(0, 9) for _ in range(5)]
    print(random_numbers)

add_random_number()
