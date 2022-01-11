import json

import pyodbc

car_data = {"name": "tesla", "engine": "electric"}
car_data_json_string = json.dumps(car_data)
print(type(car_data_json_string))

with open('new_json_file.json', 'w') as jsonfile:
    json.dump(car_data, jsonfile)

with open('new_json_file.json', 'r') as jsonfile:
    car = json.load(jsonfile)

print(type(car))
print(car)