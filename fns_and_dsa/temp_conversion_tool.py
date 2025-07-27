FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


temperature = int(input(["Enter the temperature to covert: "]))
tempType = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

if type(temperature) is not int:
    print("Invalid temperature. Please enter a numeric value.")
elif tempType == "C":
    result = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {result}°F")
elif tempType == "F":
    result = convert_to_celsius(temperature)
    print(f"{temperature}°F is {result}°C")