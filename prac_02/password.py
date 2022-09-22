"""
"""
min_length = int(input("Minimum Length:"))
password = input("Password: ")
while len(password) < min_length:
    print("Password too short!")
    password = input("Password: ")
print("*" * len(password))
