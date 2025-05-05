accounts = [
    {"username": "omar", "password": "123"},
    {"username": "ahmed", "password": "456"}
]

def get_account_by_name(name, account_list):
    return next((acc for acc in account_list if acc["username"] == name), None)

def verify_login(account):
    max_attempts = 3
    for attempt in range(max_attempts):
        entered_password = input("Password: ")
        if entered_password == account["password"]:
            print("Access granted. Welcome!")
            return True
        else:
            remaining = max_attempts - attempt - 1
            if remaining > 0:
                print(f"Incorrect password. {remaining} attempt(s) remaining.")
            else:
                print("Too many failed attempts. Access denied.")
    return False

def login():
    name_input = input("Username: ")
    account = get_account_by_name(name_input, accounts)
    
    if account:
        verify_login(account)
    else:
        print("User not found.")

if __name__ == "__main__":
    login()
