import random

def get_random_integer(n):
    return random.randint(0, n)

def get_random_boolean():
    return True if get_random_integer(1) else False

def get_random_string(length=10):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for _ in range(length):
        result += random.choice(alphabet)
    return result

def get_random_list(length=10):
    return [get_random_integer() for _ in range(length)]

def get_random_tuple(length=10):
    return tuple(get_random_list(length))

def get_random_dictionary():
    return {get_random_string(): get_random_integer() for _ in range(5)}
