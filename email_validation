def prompt_for_name():
    while True:
        name_input = input("Your Name: ").strip()
        if name_input and not name_input.isdigit():
            return name_input
        print("Invalid name. Please try again.")

def validate_email_format(email):
    if (
        "@" in email and "." in email and
        email.find("@") > 0 and
        email.rfind(".") > email.find("@") + 1 and
        not email.startswith(".") and
        not email.endswith(".") and
        " " not in email and
        ".." not in email
    ):
        return True
    return False

def prompt_for_email():
    while True:
        email_input = input("Your Email: ").strip()
        if validate_email_format(email_input):
            return email_input
        print("Invalid email format. Please try again.")

def collect_user_info():
    username = prompt_for_name()
    user_email = prompt_for_email()

    print("\n=== Collected Information ===")
    print(f"Name: {username}")
    print(f"Email: {user_email}")
    print("Email format appears to be valid.")

if __name__ == "__main__":
    collect_user_info()
