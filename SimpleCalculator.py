# Calculator

def add(x, y):
    # Function to perform addition
    return x + y

def subtract(x, y):
    # Function to perform subtraction
    return x - y

def multiply(x, y):
    # Function to perform multiplication
    return x * y

def divide(x, y):
    # Function to perform division
    return x / y

def calculator():
    # Main calculator function
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1-4): ")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        # Call add() function if choice is 1
        result = add(num1, num2)
        print("Result: ", result)
    elif choice == '2':
        # Call subtract() function if choice is 2
        result = subtract(num1, num2)
        print("Result: ", result)
    elif choice == '3':
        # Call multiply() function if choice is 3
        result = multiply(num1, num2)
        print("Result: ", result)
    elif choice == '4':
        # Call divide() function if choice is 4
        result = divide(num1, num2)
        print("Result: ", result)
    else:
        print("Invalid input. Please try again.")

if __name__ == '__main__':
    calculator()
