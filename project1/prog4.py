import re
def check_password_validity(password):
    length_check = len(password) >= 6 and len(password) <= 16
    uppercase_check = bool(re.search(r"[A-Z]", password))
    lowercase_check = bool(re.search(r"[a-z]", password))
    digit_check = bool(re.search(r"[0-9]", password))
    special_char_check = bool(re.search(r"[$#@]", password))
    if (length_check and uppercase_check and lowercase_check
            and digit_check and special_char_check):
        print("Password is valid")
    else:
        print("Password is invalid")
user_password = input("Enter your password: ")
check_password_validity(user_password)