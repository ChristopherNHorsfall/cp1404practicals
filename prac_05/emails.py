"""
CP1404/CP5632 Practical
Emails
"""
email_to_name = {}
# email = input("Email: ")
email = "christopher.horsfall@gmail.com"
email_parts = email.split("@")
text = email_parts[0]
name_parts = text.split(".")
full_name = (" ".join(name_parts)).title()
print(full_name)

