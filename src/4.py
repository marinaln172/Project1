def random_number(n):
    import random
    r = 0
    for i in range(n):
        r += random.randint(1, 6)
    return r

# Example:
print(random_number(3))
