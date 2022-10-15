"""

"""
#
# names = ["Chris", "Bob", "Alice"]
# choice = int(input("Which name?"))
# try:
#     print(f"{names[choice - 1]}")
# except IndexError:
#     print("Invalid choice")

from operator import itemgetter

score_pairs = [["Derek", 7], ["Carrie", 8], ["Bob", 6]]
string = input("Enter name then score:")
new_list = string.split()
name = new_list[0]
score = int(new_list[1])
new_score_pair = [name, score]
score_pairs.append(new_score_pair)
score_pairs.sort(key=itemgetter(1), reverse=True)
print(score_pairs)

