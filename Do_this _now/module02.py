"""Do this now"""


#
# def print_line(length):
#     print("-" * length)
#
#
# print_line(4)
#
# def print_grid(number_of_rows, number_of_columns):
#     for i in range(number_of_rows):
#         print("*" * number_of_columns)
#
#
# print_grid(3, 7)
#
import random


def main():
    name = "Christopher Horsfall"
    print("Menu: ")
    choice = input("> ").upper()
    while choice != "Q":
        if choice == "G":
            name = get_valid_name()
        elif choice == "P":
            print_greeting(name)
        elif choice == "S":
            print_secret_name(name)
        else:
            print("Invalid choice")
        print("Menu: ")
        choice = input("> ").upper()


def print_greeting(name):
    length = len(name)
    print_line(length)
    print(name)
    print_line(length)


def get_valid_name():
    name = input("Name: ")
    while name == "":
        print("Invalid name")
        name = input("Name: ")
    return name


def print_line(length):
    print("-" * length)


def print_secret_name(name):
    letters = list(name)
    random.shuffle(letters)
    print("".join(letters))


main()


#     generate_random_name()
#     print(f"Greetings {name}")
#
#
# def get_valid_name():
#     name = input("Enter name: ")
#     while name == ():
#         print("Invalid input")
#         name = input("Enter name: ")
#     return name
#
#
# def generate_random_name():
#     random_name = random.randint(0, 9)
#     return
#
#
# def print_lines():
#     pass
