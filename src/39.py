import sys

def example_function():
    # Your code here
    
if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "-f":
        example_function()
