word = input("Enter a string:")

if word.endswith("ing"):
    word = word + "iy"
else:
    word = word + "ing"

print(word)

