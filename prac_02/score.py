"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    """"Print comment based on user's score"""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    print_comment(score)


def print_comment(score):
    """Print comment based on user's valid score"""
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print(" Bad")


main()
