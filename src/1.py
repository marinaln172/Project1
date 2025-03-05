import random

def get_random_number(min_value, max_value):
    return random.randint(min_value, max_value)

def main():
    print("Random number between 1 and 6:", get_random_number(1, 6))

if __name__ == "__main__":
    main()
