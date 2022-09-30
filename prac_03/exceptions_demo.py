"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    If input is not an integer.
2. When will a ZeroDivisionError occur?
    If input for denominator is 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Yes, see below
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
