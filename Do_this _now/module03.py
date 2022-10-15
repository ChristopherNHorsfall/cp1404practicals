"""Lecture 03: Do this now"""
# FILENAME = "DTN03.txt"
# in_file = open(FILENAME,'r')
# lines = in_file.readlines()
# for line in lines:
#     if line[:1] == "#":
#         print(line)
#
with open("guitars.txt", "r") as in_file:
    in_file.readline()
    for line in in_file:
        # print(line)
        parts = line.strip().split(",")
        name = parts[0]
        year = parts[1]
        cost = float(parts[2])
        print(f"{name} was made in {year} and costs ${cost:.2f}")


