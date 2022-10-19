"""
CP1404/CP5632 Practical
Word Occurrences
Estimate: 30mins
Actual: 60min +
"""

text = input("Text: ")
# text = "this is a collection of words of nice words this is a fun thing it is"
words = text.split()
word_to_count = {}
for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1

# Sort word_to_count
# This technique is inefficient with large dictionaries
# word_to_count = dict(sorted(word_to_count.items()))

# Use list of dictionary keys sorted instead
words = list(word_to_count.keys())
words.sort()

max_length = max(len(word) for word in word_to_count)

for word, count in word_to_count.items():
    print(f"{word:{max_length}} : {count}")
