import re

text = input("Enter sentence but don' type word bad:")

new_text = re.sub("bad","good",text)

print("You're Sentence now:",new_text)
