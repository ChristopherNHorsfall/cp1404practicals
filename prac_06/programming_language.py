"""CP1404/CP5632 Practical
Estimated time: 20min"""


class ProgrammingLanguage:
    """Represents a programming language object"""

    def __init__(self, name="", is_dynamic=True, is_reflection=True, year=0):
        """"""
        self.name = name
        self.is_dynamic = is_dynamic
        self.is_reflection = is_reflection
        self.year = year

    def __str__(self):
        """"""
        if self.is_dynamic:
            dynamic_string = "Dynamic"
        else:
            dynamic_string = "Static"
        return f"{self.name}, {dynamic_string} Typing, Reflection={self.is_reflection}, First appeared in {self.year}"
