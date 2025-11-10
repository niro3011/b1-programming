import string

##variables
compliant = 0
non_compliant = 0
issues = []

##Input for password
password = input("Please put in your password:")

## functions for checking

def check_min_length(password):
    min_length = 8
    if len(password) >= min_length:
        issues.append("Too Short")
        check_min_length = True
        return
    
    else:
        check_min_length = False
        return
def has_uppercase(password):
    for char in password:
        if "A" <= char <= "Z":
            has_upper = True
            return
        if not has_upper:
            issues.append("No uppercase Letters")
            has_upper = False
            return
def has_lowercase(password):
    for char in password:
        if "a" <= char <= "z":
            has_lowercase = True
            return
        if not has_lowercase:
            issues.append("No lowercase Letters")
            has_lowercase = False
            return
def has_digit(password):
    for char in password:
        if  "0" <= char <= "9":
            has_digit = True
            return
        if not has_digit:
            issues.append("No digits")
            has_digit = False
            return
def has_special_char(password):
    for char in password:
        if  "!" <= char <= "/" or ":" <= char <= "@" or "{" <= char <= "~" :
            has_special_char = True
            return
        if not has_special_char:
            issues.append("No special characters")
            has_special_char = False
            return

def has_noissues(password):
    if len(issues) == 0:
        print(f"PASS - {password} - Meets all requierments")
        return
    else:
        text = ",".join(issues)
        print(f"FAIL: {password} - {text} please fix")
        return

def validate_password(password):
    has_lowercase(password)
    has_digit(password)
    has_special_char(password)
    has_uppercase(password)
    check_min_length(password)
    has_noissues(password)

validate_password(password)
    
