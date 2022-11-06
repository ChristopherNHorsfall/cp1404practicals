"""

"""
import operator
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
            display_projects(projects)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            pass
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid input")
        print(MENU)
        choice = input(">>> ").upper()


def update_project(projects):
    """"""
    for i, project in enumerate(projects):
        print(i, project)
    project_choice = int(input("Project choice: "))
    new_percentage = int(input("New Percentage: "))
    new_priority = int(input("New Priority: "))
    chosen_project = projects[project_choice]
    print(chosen_project)
    chosen_project.completion_percentage = new_percentage
    if new_priority != "":
        chosen_project.priority = new_priority
    print(chosen_project)


def display_projects(projects):
    """Display list of projects organised into groups and sorted by priority"""
    incomplete_projects = [project for project in projects if project.completion_percentage < 100]
    if len(incomplete_projects) > 0:
        incomplete_projects.sort(key=operator.attrgetter("priority"))
        print("Incomplete projects:")
        for project in incomplete_projects:
            print(f"  {project}")
    complete_projects = [project for project in projects if project.completion_percentage == 100]
    if len(complete_projects) > 0:
        complete_projects.sort(key=operator.attrgetter("priority"))
        print("Completed projects")
        for project in complete_projects:
            print(f"  {project}")


def load_projects(filename):
    """Load data from file and return list of project objects"""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        projects = []
        in_file.readline()  # Skip header line
        for line in in_file:
            project_parts = line.strip().split("\t")
            print(project_parts)
            name, start_date_string, priority, cost_estimate, completion_percentage = project_parts
            start_date = datetime.datetime.strptime(start_date_string, "%d/%m/%Y").date()
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
    print(start_after_date)
    for project in projects:
        if project.start_date > start_after_date:
            print(project)


main()
