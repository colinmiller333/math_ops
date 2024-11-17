def divide_numbers(a, b):
    """Divides two numbers and returns the result."""
    if b == 0:
        return "Cannot divide by 0, try again!"
    return a / b  # Potential division by zero error

def multiply_numbers(a, b):
    """Multiplies two numbers and returns the result."""
    return a * b  

if __name__ == "__main__":
    x = 10
    y = 0
    result = divide_numbers(x, y)
    print(f"The result of division is: {result}")

    x2 = 5
    y2 = 4
    result2 = multiply_numbers(x2, y2)
    print(f"The result of multiplication is: {result2}")