"""
CP1404/CP5632 Practical
Intermediate Exercises
Hex Colours
"""

COLOUR_TO_CODE = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff",
                  "Alizarin crimson": "#e32636",
                  "Amaranth": "#e52b50",
                  "Amber": "#ffbf00",
                  "Amethyst": "#9966cc",
                  "AntiqueWhite": "#faebd7",
                  "AntiqueWhite1": "#ffefdb",
                  "AntiqueWhite2": "#eedfcc"}

colour = input("Enter colour name: ").lower()
# Change all keys to lowercase
lowercase_colour_to_code = {colour.lower(): code for (colour, code) in COLOUR_TO_CODE.items()}
while colour != "":
    try:
        print(f"'{colour}' is {lowercase_colour_to_code[colour]}")
    except KeyError:
        print(f"{colour} is not in Dictionary")
    colour = input("Enter colour name: ")

