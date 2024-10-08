# Python calculator
operator = input("Enter an operator(+ - * /): ")
if operator == "-" or operator == "+" or operator == "*" or operator == "/":
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2st number: "))
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    print(result)
else:
    print(f"Operator is not valid")


# Weight Converter
weight = float(input("Enter your weight"))
unit = input("Kilograms or pounds? (K or L)")
if unit == "K":
    weight = weight * 2.205
    unit = "kgs."
    print(f"Your weight is: {weight} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "lbs."
    print(f"Your weight is: {weight} {unit}")
else:
    print(f"{unit} is not valid")

# temperature conversion program
unit_temp = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))
if unit_temp == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp}°F")
elif unit_temp == "F":
    temp = round((temp - 32) * 5 / 9)
    print(f"The temperature in Celcius is: {temp}°C")

else:
    print(f"{unit_temp}is an invalid unit of measurement")
