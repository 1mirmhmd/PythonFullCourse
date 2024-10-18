name = input("Enter your full name : ")
# name_len = len(name)
# name_fnd = name.find(" ")
# name_rfnd = name.rfind("a")
# name_cap = name.capitalize()
# name_up=name.upper()
# name_lw=name.lower()
# name_isdgt=name.isdigit()
# name_isalp=name.isalpha()
# name_cnt=name.count("A")
# name_rep=name.replace("A","a")
# print(help(str))
# print(name_rep)

# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username : ")
if len(username) > 12:
    print("Your username can`t be more than 12 characters!")
elif not username.find(" ") == -1:
    print("Your username  can`t contain spaces!")
elif not username.isalpha():
    print("Your username  can`t contain digits!")
else:
    print(f"Welcome {username}")
