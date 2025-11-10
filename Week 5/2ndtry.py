import random
import string

password = input("Hier bitte Passwort Danke:")

def check_min_length(password,min_len=8):
    if len(password) >= min_len:
        return True
    else:
        return False

def has_uppercase(password):
    return any(char.isupper() for char in password)

def has_lowercase(password):
    return any(char.islower() for char in password)

def has_digit(password):
    return any(char.isdigit() for char in password)

def has_special_char(password):
    special_chars = "!@#$%^&*()-_=+][]}{;:'\",.<>?/\\|`~"
    return any(char in special_chars for char in password)

def validation(password):
    if (has_special_char(password) and has_digit(password) and has_lowercase(password) and has_uppercase(password) and check_min_length(password)):
       print(f"{password} is good no complaints")
    else:
        issues = []
        if not has_digit(password):
            issues.append("No digits")
        if not has_lowercase(password):
            issues.append("No lowercase letters")
        if not has_uppercase(password):
            issues.append("No uppercase letters")
        if not has_special_char(password):
            issues.append("No special characters")
        if not check_min_length(password):
            issues.append("Not minimum length")
        
        errormessage = ",".join(issues)
        
        print(f"FAIL: {password} - {errormessage}")



validation(password)