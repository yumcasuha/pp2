import json

student = {
    "name": "Amina",
    "age": 18,
    "grades": {"math": 95, "english": 88}
}

json_string = json.dumps(student, indent=4)
print(json_string)



