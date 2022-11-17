"""

"""


class Project:
    """Represents a Project object"""

    def __init__(self, name="", start_date="00/00/0000", priority=0, cost_estimate=0.00, completion_percentage=0):
        """Initalise a Project object"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        """"""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}% "
