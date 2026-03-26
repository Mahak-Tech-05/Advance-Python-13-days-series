import re

username = input("Enter youre Username")
pattern = r"^[A-Za-z]"# r=raw string , ^=start string [A-Z]=Uppercase a-z=lowercase

result = re.match(pattern , username)

if result:
    print("Correct username")

else:
    print(" you're username is not accepted Start username with alphabets")
