import re

email = input("Enter you're email id:")
pattern = r"^[\w\.-]+@[\w\,-]+\.\w+$"#r = raw string ^ = start string [\w\.-]+ = username part \w - letters+numbers+underscore . -> dot ,- ->hyphen
                                     #@ -> must have this symbol after username part [\w\.-]+ -> Domain name(gmail,yahho) ,\. -> dot,\w+ extension(com,in,org)

if re.match(pattern , email):
    print("You're email id is valid conguralations!")

else:
    print("Sorry invalid id!")
