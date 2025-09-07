#   asking the user to create ther username, but there username can't contain spaces, digits, and should not exceed more than 12 characters.
#   asking the user input to create a username.
username = input("Enter your username (your username can't contain spaces, digits, and should not exceed more than 12 characters): ")
#   checking if the username does not contain spaces, digits, and should not exceed more than 12 characters.
check_spaces_and_digits = username.isalpha()
check_character = len(username)
while check_spaces_and_digits == False or check_character > 12 or username == "":
#   if it does contain spaces, digits, and exceed more than 12 characters, it will print out "Invalid username! Please Try again later."
    print("Invalid username! Please Try again later.")
    username = input("Enter your username (your username can't contain spaces, digits, and should not exceed more than 12 characters): ")
    check_spaces_and_digits = username.isalpha()
    check_character = len(username)
#   if it does not contain spaces, digits, and should not exceed more than 12 characters, it will print out "You have successfully created your username!😊"
print("You have successfully created your username!😊")