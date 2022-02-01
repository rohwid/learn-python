import json

class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age


def encode_user(o):
    if isinstance(o, User):
        # just the key of the class name is important, the value can be arbitrary.
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError(f"Object of type '{o.__class__.__name__}' is not JSON serializable")

user = User("Max", 27)
encoded_user = json.dumps(user, default=encode_user)
print(encoded_user)

with open('person3.json', 'w') as f:
    json.dump(encoded_user, f, indent=4)