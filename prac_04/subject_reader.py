"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    # print(data)
    display_data(data)


def get_data():
    """Read data from file formatted like: subject_data.txt,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        # print(parts)  # See if that worked
        # print("----------")
        subject = [part for part in parts]
        # print(subject)
        data.append(subject)
    input_file.close()
    return data


def display_data(data):
    for details in data:
        subject, teacher, number_of_students = details
        print(f"{subject} is taught by {teacher:12} and has {number_of_students:3} students")


# def display_details(subject, teacher, number_of_students):


main()
