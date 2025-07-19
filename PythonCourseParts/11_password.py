# Validates a password and determines if it's strong or weak

user_password = input("Enter your password: ")

# Boolean list, first item for length, second for digits, third for uppercase
pass_validation_list = []

# Can be done with dictionaries too
# pass_validation_dict = {<<element1_key1>>:<<element1_key2>>, <<element2_key3>>:<<element2_key4>>}
# pass_validation_dict["element1_key1"] = <<new element1_key2 value>>

# Checks length
if len(user_password) >= 10:
    pass_validation_list.append(True)
else:
    pass_validation_list.append(False)

# Checks if password contains number
password_digit = 0
for char in user_password:
    if char.isdigit():
        password_digit += 1

if password_digit >= 4:
    pass_validation_list.append(True)
else:
    pass_validation_list.append(False)
        
# Check if password contains uppercase letter
password_character = 0
for char in user_password:
    if char.isupper():
        password_character += 1

if password_character >= 2:
    pass_validation_list.append(True)
else:
    pass_validation_list.append(False)

# all checks for boolean list values (if all are true returns true)
# all also checks for second key value of dictionaries
if all(pass_validation_list):
    print("Your password is very strong!")
else:
    print("Your password is weak")

print(pass_validation_list)
    