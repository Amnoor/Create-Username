# create username
# this is a project I made to practice my skills, it let's you create username with a set of rules that you cant break
# rules:
# username can't contain spaces, digits, and should not exceed more than 12 characters

# ask user for username
username = input("Enter your username (your username can't contain spaces, digits, and should not exceed more than 12 characters): ")
# check if username is valid
check_spaces_and_digits = username.isalpha()
check_character = len(username)
# if username is valid, then I wille set the variable is_valid to True
if check_spaces_and_digits == False and check_character >= 12 and username == "":
    is_valid = True
# else, I will set the variable is_valid to False
else:
    is_valid = False
# while the variable is_valid is True
while is_valid:
#   I will print a Error Message and ask the user to try again
    print("Invalid username! Please Try again later.")
#   ask user for username again
    username = input("Enter your username (your username can't contain spaces, digits, and should not exceed more than 12 characters): ")
#   check if username is valid again
    check_spaces_and_digits = username.isalpha()
    check_character = len(username)
#   if username is valid, then I wille set the variable is_valid to True and repeat this while loop
    if check_spaces_and_digits == False and check_character >= 12 and username == "":
        is_valid = True
#   else, I will set the variable is_valid to Fals, so the while loop will end
    else:
        is_valid = False
# print a success message
print("You have successfully created your username!😊")