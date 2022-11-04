"""

"""

from prac_07.project import Project

MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new " \
       "project\n- (U)pdate project\n- (Q)uit "
FILENAME = "projects.txt"


def main():
    """"""
    print(MENU)
    choice = input(">>> ".upper())
    while choice != "q":
        if choice == "L":
            pass
        elif choice == "S":
            pass
        elif choice == "D":
            pass
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid input")
        print(MENU)
        choice = input(">>> ".upper())


def load_projects(filename):
    """Load projects from file and create list of project objects"""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        projects = []
        in_file.readline()  # Skip header line
        for line in in_file:
            project_parts = line.strip().split("    ")
            name, start_date, priority, cost_estimate, completion_percentage = project_parts
            project_to_add = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project_to_add)
