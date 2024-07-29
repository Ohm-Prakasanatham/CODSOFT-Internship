def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def calculator():
    print("Welcome to the Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice(1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                result = divide(num1, num2)
                if result == "Error! Division by zero.":
                    print(result)
                else:
                    print(f"{num1} / {num2} = {result}")

        else:
            print("Invalid input. Please select a valid operation (1/2/3/4).")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

if __name__ == "__main__":
    calculator()
