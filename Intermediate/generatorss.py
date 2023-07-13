"""
    Generator are function that return a object that can be iterated over
"""

def mygenerator():
    yield 1
    yield 2
    yield 3

#   create generator object
g = mygenerator()

# # loop
# for i in g:
#     print(i)

value = next(g)
print(value)

value = next(g)
print(value)

value = next(g)
print(value)

# Stop looping if doesn't find another yield statement
# sort()