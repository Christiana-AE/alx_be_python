first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

if operation == "+":
    print(f"The result is {first + second}.")
elif operation == "-":
    print(f"The result is {first - second}.")
elif operation == "*":
    print(f"The result is {first * second}.")
elif operation == "/" and second != 0:
    print(f"The result is {first / second}.")
elif operation == "/" and second == 0:
    print(f"Cannot divide by zero.")
