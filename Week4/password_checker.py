import string

MINIMUM_LENGTH = 5
MAXIMUM_LENGTH = 15
UPPER = string.ascii_uppercase
LOWER = string.ascii_lowercase
DIGITS = string.digits
SPECIAL = string.punctuation

def check_password(user_password, validator):
    for each in user_password:
        if each in validator:
            return True
    return False

print("Your password must be between 5 and 15 characters, and contain\n\t1 or more uppercase characters\n\t1 or more lowercase characters\n\t1 or more numbers\n\tand 1 or more special characters: !@#$%^&*()_-­‐=+`~,./o'[]\<>?O{}|")
user_password = input("Please enter a valid password")

while True:
    if len(user_password) < 5 or len(user_password) > 15:
        print("Invalid password, Length requirement is not met")
        user_password = input(">")
    elif not check_password(user_password, UPPER):
        print("Invalid password, Uppercase requirement is not met")
        user_password = input(">")
    elif not check_password(user_password, LOWER):
        print("Invalid password, Lowercase requirement is not met")
        user_password = input(">")
    elif not check_password(user_password, DIGITS):
        print("Invalid password, Digits requirement is not met")
        user_password = input(">")
    elif not check_password(user_password, SPECIAL):
        print("Invalid password, Special characters requirement is not met")
        user_password = input(">")
    else:
        break
print("Password accepted")