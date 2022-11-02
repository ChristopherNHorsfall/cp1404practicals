"""CP1404/CP5632 Practical
Estimated time: 60min"""
CURRENT_YEAR = 2022
VINTAGE_AGE = 50


class Guitar:
    """Represents a Guitar object"""

    def __init__(self, name="", year=0, cost=0):
        """Initialise guitar object"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Display details of guitar object"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Calculate age of guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Returns if guitar age is vintage"""
        return self.get_age() >= VINTAGE_AGE
