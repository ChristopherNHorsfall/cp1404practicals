"""
CP1404/CP5632 Practical
Emails
"""


def main():
    email_to_name = {}
    # email = input("Email: ")
    email = "christopher.horsfall@gmail.com"
    full_name = extract_full_name(email)
    # print(full_name)
    email_to_name[email] = full_name
    print(email_to_name)


def extract_full_name(email):
    email_parts = email.split("@")
    text = email_parts[0]
    name_parts = text.split(".")
    return (" ".join(name_parts)).title()
