# conditional expressions = A one-line shortcut for this if-else statement(ternary operator)
#   Print or assign one of two values based on a condition
#   X if condition else Y
num = 5
a = 6
b = 7
age = 25
temperature = 20
user_role = "admin"

# print("Positive" if num > 0 else "Negative")
# result = "EVEN" if num % 2 == 0 else "ODD"
# max_num = b if b > a else a
# status= "Adult"if age>18 else "Chiild"
# weather = "Hot" if temperature > 20 else "Cold"
access_level = "Full Access" if user_role == "admin" else "Limited Access"

print(access_level)
