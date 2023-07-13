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


# Execution of a generator
def countdown(num):
    print("Starting")
    while num > 0:
        yield num
        num -= 1

# object
cd = countdown(4)

# get first value
value = next(cd)
print(value)
