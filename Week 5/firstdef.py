
def get_credentials():
    return input("User: "), input("Pass: ")

def validate_password(pwd):
    return len(pwd) >= 8

def authenticate(user, pwd):
    if not validate_password(pwd):
        return False
    return user == "admin"

user, pwd = get_credentials()

if authenticate(user, pwd):
    print("Welcome!")
else:
    print("Login failed")