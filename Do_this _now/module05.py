"""

"""
# names = ["Abe", "Bob", "Chris"]
# ages = [12, 32, 35]
#
#
# # max_age = max(ages)
# # max_age_index = ages.index(max_age)
# # print(names[max_age_index])
# # print(ages[max_age_index])
#
#
# def find_oldest(names, ages):
#     # return names[ages.index(max(ages))]
#     oldest_age = -1
#     oldest_index = -1
#     for i, age in enumerate(ages):
#         if age > oldest_age:
#             oldest_age = age
#             oldest_index = i
#     return names[oldest_index]
#
#
# print(find_oldest(names, ages))

name_to_age = {"Bill": 21, "Jane": 4, "Sven": 56}

name = input("Name: ")
age = int(input("Age: "))
name_to_age.update({name: age})
max_length = max(len(name) for name in list(name_to_age.keys()))

for name, age in name_to_age.items():
    print(f"{name:{max_length}} -\t{age:3}")
