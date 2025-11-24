def get_number(prompt):
    """Validate and return a number."""
    while True:
        try:
            return eval(input(prompt))
        except (ValueError, SyntaxError):
            print("Invalid input! Please enter a valid number.")

def get_operation():
    """operations"""
    valid_ops = ['+', '-', '*', '/']
    
    while True:
        op = input("Choose operation (+, -, *, /): ")
        if op in valid_ops:
            return op
        else:
            print("Invalid operation! Please choose +, -, *, or /.")

def calculate(num1, num2, operation):
    """Perform the selected operation."""
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Error: Division by zero is not allowed!"
        return num1 / num2

def calculator():
    print("---- Simple Calculator ----")
    
    number1 = get_number("Enter first number: ")
    number2 = get_number("Enter second number: ")
    operation = get_operation()

    result = calculate(number1, number2, operation)

    print(f"Result: {result}")

# Run the calculator
calculator()
