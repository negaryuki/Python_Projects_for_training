def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def simple_calculator():
    print("Simple Calculator")
    print("Operations: ")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("Enter 'q' to quit")

    while True:
        choice = input("Enter operation number (1/2/3/4) or 'q' to quit: ")

        if choice == 'q':
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please try again.")
            continue

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        else:
            result = divide(num1, num2)

        print(f"Result: {result}")

if __name__ == "__main__":
    simple_calculator()
