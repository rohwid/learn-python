import json

with open('person2.json', 'r') as f:
    person = json.load(f)
    print(person)