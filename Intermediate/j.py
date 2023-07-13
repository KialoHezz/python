"""
    Encode and Decode

    =========================================
    1. Python
        # dict
        # list, tuple
        # str
        # int, long, float
        # True
        # False
        # None

    2. JSON
        # object
        # array
        # string
        # number
        # true
        # false
        # null
    Serialization from python to json
"""
import json
from typing import Any

# python object into JSON
# person = {
#     "name": "Hezron",
#     "age": 30,
#     "city": "Nairobi",
#     "hasChildren": False,
#     "title": ["Software Developer", "Graphic Designer"]
# }

# personJSON = json.dumps(person, indent=4, sort_keys=True)
# print(personJSON)

# # # open file with mode of write
# # with open('person.json', 'w') as file:
# #     # dump person object
# #     json.dump(person, file, indent=4)


# # back to python object, it callled deseriliazation.

# person = json.loads(personJSON)
# print(person)


# Custom Class
class User:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

# create object
user = User('Hezron K.', 19)

# custom encoding function
def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age':o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not JSON Serializable')
    
from json import JSONEncoder

class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):           
            return {'name': o.name, 'age':o.age, o.__class__.__name__: True}
        
        return JSONEncoder.default(self, o)


        
        


userJSON = json.dumps(user, cls=UserEncoder)
# OR
userJSON = UserEncoder().encode(user)
print(userJSON)