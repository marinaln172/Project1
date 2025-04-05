import random

def game():
    # Generate two random numbers between 0 and 100
    number1 = random.randint(0, 100)
    number2 = random.randint(0, 100)

    if number1 < number2:
        print("Number 1 is smaller than Number 2.")
    elif number1 > number2:
        print("Number 1 is larger than Number 2.")
    else:
        print("Numbers are equal.")

if __name__ == "__main__":
    game()
