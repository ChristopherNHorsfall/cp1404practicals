"""
CP1404/CP5632 - Practical
Files
"""

# Program 1
name = input("Enter name: ")
with open("name.txt", "w") as out_file:
    print(name, file=out_file)

# Program 2
with open("name.txt", "r") as in_file:
    name = in_file.read().strip()
    print(f"Your name is {name}")

# Program 3
with open("numbers.txt", "r") as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
    result = first_number + second_number
print(result)

# Program 4
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        number = int(line)
        total += number
print(total)
