"""
CP1404/CP5632 Practical
Word Occurrences
Estimate: 30mins
Actual: 30min +
"""

# text = input("Text: ")
text = "this is a collection of words of nice words this is a fun thing it is"
words = text.split()
word_to_count = {}
for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1
dict(sorted(word_to_count.items()))
print(word_to_count)





