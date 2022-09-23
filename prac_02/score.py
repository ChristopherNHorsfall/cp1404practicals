"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    """"Print comment based on user's score"""
    score = generate_random_score()
    # score = float(input("Enter score: "))
    # while score < 0 or score > 100:
    #     print("Invalid score")
    #     score = float(input("Enter score: "))
    print_comment(score)


def print_comment(score):
    """Print comment based on user's valid score"""
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


def generate_random_score():
    """Generate random score between 0 and 100"""
    score = random.randint(0, 100)
    return score


main()
