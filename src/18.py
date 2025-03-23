class SimpleProject1:
    def __init__(self):
        self.numbers = [1, 2, 3]

    def add_numbers(self):
        return sum(self.numbers)

# Example usage
project = SimpleProject1()
print(project.add_numbers())  # Output: 6
