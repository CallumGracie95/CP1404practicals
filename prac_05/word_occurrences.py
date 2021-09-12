"""
CP1404/ Practical
Word occurring in a string
"""
word_count_dict = {}
text = input("String: ")
words = text.split()
for word in words:
    occurrence_count = word_count_dict.get(word, 0)
    word_count_dict[word] = occurrence_count + 1

words = list(word_count_dict.keys())
words.sort()
longest_word = max(len(word) for word in words)

for word in words:
    print(f"{word:{longest_word}} : {word_count_dict[word]}")
