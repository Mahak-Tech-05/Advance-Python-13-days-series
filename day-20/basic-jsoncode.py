import json

data = {
    "name":"Ram",
    "age":19,
    "course":"Python"
    }
json_data = json.dumps(data)#covert python dictionary to json dictonary 
print(json_data)
