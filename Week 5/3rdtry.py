import random
import string
print("Please make sure your password meets the requirements.")
password = input("Please insert your password:")

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
    check = {
        "has digit": (has_digit, "No digits"),
        "has lowercase": (has_lowercase, "No lowercase"),
        "has uppercase": (has_uppercase, "No uppercase"),
        "has special char": (has_special_char, "No special characters"),
        "has minumum length": (check_min_length, "Not minimum length")        
    }
    affirmation = ["i know you are able to choose a strong password :-)", "you will be able to secure youre account at some point. ;-)","choose something far better please :-("]
    aff = random.choice(affirmation)
    succtest = ["Great Job, you can follow instructions", "Great success", "you are the best at choosing a password based on specific requirements"]
    successtext = random.choice(succtest)

    results = {}
    issues = []

    for name, (function, errormessage) in check.items():
        result = function(password) 
        results[name] = result   
        if not result:
            issues.append(errormessage)
            
    if all(results.values()):
        print(f"{password} is fine - no errors found")
        print(successtext)
    else:
        print(f"FAIL: {password} please fix the following issues: {', '.join(issues)}")
        print(aff)
    
    print("Details:")
    for key, value in results.items():
        print(f"{key}: {'Y' if value else 'X'}")

validation(password)