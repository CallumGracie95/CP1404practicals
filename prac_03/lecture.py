# name = "Bobby McAardvark"
# VOWELS = "aeiou"
# vowel_count = 0
# for char in name:
#     if char.lower() in VOWELS:
#         vowel_count += 1
# print(f"Out of {len(name)} characters, {name} had {vowel_count} vowels")

names = ["JameS", "Sally"]
for i in range(len(names)):
    names[i] = names[i].title()
print(names)

