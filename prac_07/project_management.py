"""

"""
import datetime
from prac_07.project import Project

MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new " \
       "project\n- (U)pdate project\n- (Q)uit "
FILENAME = "projects.txt"


def main():
    """"""
    projects = load_projects(FILENAME)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "q":
        if choice == "L":
            pass
        elif choice == "S":
            pass
        elif choice == "D":
            for project in projects:
                print(project)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid input")
        print(MENU)
        choice = input(">>> ").upper()


def load_projects(filename):
    """Load data from file and return list of project objects"""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        projects = []
        in_file.readline()  # Skip header line
        for line in in_file:
            project_parts = line.strip().split("\t")
            print(project_parts)
            name, start_date, priority, cost_estimate, completion_percentage = project_parts
            start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
            priority = int(priority)
            cost_estimate = float(cost_estimate)
            completion_percentage = int(completion_percentage)
            project_to_add = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project_to_add)
    return projects


def filter_projects(projects):
    """"""
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    # Convert string to date object
    start_after_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    for project in projects:
        if project.start_date > start_after_date:
            print(project)



main()
