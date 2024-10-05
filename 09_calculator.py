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


