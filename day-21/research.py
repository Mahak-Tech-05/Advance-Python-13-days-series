import re

text = input("Enter Product: ")

products = ["Mobile", "Phone", "Headset"]

found = False

#here re.ignorecase means telling python to ignoe differencebetwee upper case and lower case                                                                             
for item in products:
    if re.search(item, text, re.IGNORECASE):
        found = True 
        break

if found:
    print("Product found")
else:
    print("Product is not available in our list!")
