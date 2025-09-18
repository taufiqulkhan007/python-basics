# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

if __name__ == "__main__":
    print("Simple Calculator")
    print(add(10, 5))
    print(subtract(10, 5))
    print(multiply(10, 5))
    print(divide(10, 0))
