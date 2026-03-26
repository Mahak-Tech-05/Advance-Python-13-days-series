import re

text = input("Enter the sentence in which you wnat to search :")
result = re.findall("ram",text)

print("This no. of ram name you used:",result)
