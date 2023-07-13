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

# python object into JSON
person = {
    "name": "Hezron",
    "age": 30,
    "city": "Nairobi",
    "hasChildren": False,
    "title": ["Software Developer", "Graphic Designer"]
}

personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)

# # open file with mode of write
# with open('person.json', 'w') as file:
#     # dump person object
#     json.dump(person, file, indent=4)


# back to python object, it callled deseriliazation.

person = json.loads(personJSON)
print(person)