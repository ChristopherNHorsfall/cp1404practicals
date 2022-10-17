"""
CP1404/CP5632 Practical
Word Occurrences
Estimate: 30mins
Actual: 30min +
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
word_to_count = dict(sorted(word_to_count.items()))

max_length = max(len(word) for word in word_to_count)

for word, count in word_to_count.items():
    print(f"{word:{max_length}} : {count}")
