def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

numbers = [1, 2, 3, 4, 5]
average = calculate_average(numbers)
print("Average of the numbers:", average)
