"""
CP1404/CP5632 Practical
"Quick Pick" Lottery Ticket Generator
"""
import random

MIN_NUMBER = 1
MAX_NUMBER = 45
VALUES_PER_LINE = 6


def main():
    number_of_lines = int(input("How many quick picks? "))
    lottery_ticket = generate_lottery_ticket(number_of_lines)
    display_lottery_ticket(lottery_ticket)


def display_lottery_ticket(lottery_ticket):
    for line in lottery_ticket:
        for value in line:
            print(f"{value:4}", end="")
        print(" ")


def generate_lottery_ticket(number_of_lines):
    lottery_ticket = []
    for i in range(number_of_lines):
        line = []
        lottery_ticket.append(line)
        for j in range(VALUES_PER_LINE):
            value = random.randint(MIN_NUMBER, MAX_NUMBER)
            line.append(value)
    return lottery_ticket


main()
