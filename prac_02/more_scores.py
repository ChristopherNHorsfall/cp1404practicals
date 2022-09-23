"""
Ask the user for a number of scores.
Generate that many random numbers (scores) between 0 and 100 inclusive
For each of those scores, write the "result" to a file called results.txt
"""
import random


def main():
    """ """
    outfile = open('Results.txt', 'w')
    number_of_scores = int(input("Enter number of scores: "))
    for i in range(number_of_scores):
        score = generate_random_score()
        comment = determine_comment(score)
        outfile.write(f"{score} is {comment}")
    outfile.close()


def determine_comment(score):
    """Determine comment based on user's valid score"""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def generate_random_score():
    """Generate random score between 0 and 100"""
    score = random.randint(0, 100)
    return score


main()
