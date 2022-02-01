import json
from json import JSONEncoder

class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

class UserEncoder(JSONEncoder):
    
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        
        # Let the base class default method handle other objects or raise a TypeError
        return JSONEncoder.default(self, o)

user = User("Max", 27)

encoded_user = json.dumps(user, cls=UserEncoder)
print(encoded_user)

encoded_user = UserEncoder().encode(user)
print(encoded_user)