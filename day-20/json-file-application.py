import json

#creating data
students=[
    {"name":"Ram","marks":90},
    {"name":"Sham","marks":80},
    {"name":"Basanti","marks":95}
    ]

#save data to json file
with open("students.json","w")as  file:
    json.dump(students,file,indent=4)#make file clean readable

print("Data saved succesfully")

#read data from json file
with open("students.json","r")as file:
    data = json.load(file)#data store 

print("\n Data loaded succesfully")

#use data
for student in data:
    print(student["name"],"-",student["marks"])
