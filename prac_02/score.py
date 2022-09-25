"""
Prac 02 : Score
"""
import random


def main():
    """"Print comment based on score"""
    score = generate_random_score()
    # score = get_user_score(score)
    print(f"Score : {score}")
    print_comment(score)


def get_user_score():
    """Get user score from 0 to 100 inclusive."""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


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
