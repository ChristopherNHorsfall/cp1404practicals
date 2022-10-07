"""
CP1404/CP5632 Practical
Intermediate Exercises

"""

# Basic list operations

NUMBER_OF_NUMBERS = 5
# numbers = [5, 20, 1, 2, 3]
numbers = []
for i in range(NUMBER_OF_NUMBERS):
    number = int(input("Number: "))
    numbers.append(number)


print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
average = sum(numbers) / len(numbers)
print(f"The average of the numbers is {average}")

# Woefully inadequate security checker

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Enter username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
