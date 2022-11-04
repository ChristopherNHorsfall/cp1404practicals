"""
CP1404/CP5632 Practical
Estimated time: 60min
Testing Guitar class
"""

from prac_06.guitar import Guitar

Gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
Another_Guitar = Guitar("Another Guitar", 2013, 100)

print(f"Gibson get_age() - Expected 100. Got {Gibson.get_age()}")
print(f"Another_Guitar get_age() - Expected 9. Got {Another_Guitar.get_age()}")
print(f"Gibson is_vintage() - Expected True. Got {Gibson.is_vintage()}")
print(f"Another_Guitar is vintage() - Expected False. Got {Another_Guitar.is_vintage()}")