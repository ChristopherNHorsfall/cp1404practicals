"""
Prac 02 : Score Menu
"""
MENU = "(E)nter Score\n(P)rint Result\nPrint (S)tars\n(Q)uit"


def main():
    """get valid score from user, comment on such score, and print stars based on score."""
    score = 0
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "E":
            score = get_valid_score()
        elif choice == "P":
            comment = determine_comment(score)
            print(f"{score} is {comment}")
        elif choice == "S":
            print("*" * score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def get_valid_score():
    """Get score from user in the range of 0 to 100 inclusive"""
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


def determine_comment(score):
    """Determine comment based on user's valid score"""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
