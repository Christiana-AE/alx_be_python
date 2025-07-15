first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        print(f"The result is {first + second}.")
    case "-":
        print(f"The result is {first - second}.")
    case "*":
        print(f"The result is {first * second}.")
    case "/":
        if second != 0:
            print(f"The result is {first / second}.")
        else:
            print("Cannot divide by zero.")
