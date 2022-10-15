"""
CP1404/CP5632 Practical
Emails
"""


def main():
    """Create dictionary of emails to names using user input"""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        full_name = extract_full_name(email)
        is_full_name = input(f"Is your name {full_name}? (Y/n) ")
        if is_full_name.upper() != "Y" and is_full_name != "":
            full_name = input("Name: ")
        email_to_name[email] = full_name
        email = input("Email: ")
    print("")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_full_name(email):
    """Extract full name from email address"""
    email_parts = email.split("@")
    email_name = email_parts[0]
    name_parts = email_name.split(".")
    full_name = (" ".join(name_parts)).title()
    return full_name


main()
