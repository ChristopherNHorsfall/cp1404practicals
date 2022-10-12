"""
CP1404/CP5632 Practical
"Quick Pick" Lottery Ticket Generator
"""
import random

MIN_NUMBER = 1
MAX_NUMBER = 45
VALUES_PER_LINE = 6


def main():
    """Creates a 'Quick Pick' lottery ticket based on user input"""
    number_of_lines = int(input("How many quick picks? "))
    lottery_ticket = generate_lottery_ticket(number_of_lines)
    display_lottery_ticket(lottery_ticket)


def generate_lottery_ticket(number_of_lines):
    """Generates a lottery ticket based on the number of 'quick picks' (number_of_lines).
    Each quick pick does not have repeated values and is sorted once created"""
    lottery_ticket = []
    for i in range(number_of_lines):
        available_numbers = list(range(MIN_NUMBER, MAX_NUMBER + 1))  # Recreated at each line
        line = []
        lottery_ticket.append(line)
        for j in range(VALUES_PER_LINE):
            value = random.choice(available_numbers)
            available_numbers.remove(value)
            line.append(value)
        line.sort()  # Sort now rather than in display function, no benefit otherwise

    return lottery_ticket


def display_lottery_ticket(lottery_ticket):
    """Displays lottery ticket neatly"""
    for line in lottery_ticket:
        for value in line:
            print(f"{value:4}", end="")
        print(" ")


main()
