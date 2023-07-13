"""
    random methods such as:
        1. uniform()
        2. randint()
        3. random()
        ##########################
     
"""

import random

a =  random.uniform(1, 10)
# statics
a = random.normalvariate(0, 1)

# print(a)

mylist = list("ABCDEFGH")
b = random.choice(mylist)
print(b)
