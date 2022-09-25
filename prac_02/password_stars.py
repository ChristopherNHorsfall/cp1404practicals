"""
Prac 02 : Password Stars
Turns passwords into a string of stars
"""


def main():
    """Turns passwords into a string of stars"""
    password = get_password()
    print_stars(password)


def print_stars(password):
    """Print a string of stars equal to the length of the password"""
    print("*" * len(password))


def get_password():
    """Get a valid password from user"""
    min_length = int(input("Minimum Length:"))
    password = input("Password: ")
    while len(password) < min_length:
        print("Password too short!")
        password = input("Password: ")
    return password
