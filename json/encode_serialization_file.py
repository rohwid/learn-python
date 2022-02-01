import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

with open('person1.json', 'w') as f:
    json.dump(person, f)

with open('person2.json', 'w') as f:
    json.dump(person, f, indent=4)