"""
    PYTHON QUESTION :
    ========================= 1. create a python class called "Students" which takes a list of a student_name as input.

    The method shld generate random marks(between 60 and 100) => 60 & 100 are included
     
        second = random.randint(1, 6)
    for each student and store them in  a dictionary where the student name is the key and mark is the value, the class shld have a method to ger=nerate_result that prints the student name along with their corresponding marks

"""
import random

class Students:
    #  constructor
     def __init__(self):
         self.student_marks = {}

     def generate_marks(self, student_names):
        for name in student_names:
            mark = random.randint(60, 100)
            self.student_marks[name] = mark

     def display_results(self):
         for name, mark in self.student_marks.items():
             print(f"{name} : {mark}")
         
# list of students
student_list = ["Baraka", "Bob", "Hezron", "Charles", "Bobel"]

# instantiated the obj
students_obj = Students()
# students_obj.generate_marks(student_list)
# students_obj.display_results()

"""
    Write a python program that takes a sentence as input and counts the frequency of each word in the sentence. Display the word frequencies in descending order
"""
# prompt user to key in the sentence
# user_input = input("write your sentence: ")

# split the words => split method returns a array
# words = user_input.split(" ")

# dictionary
# word_frequencies = {}
# iterate the array
# for word in words:
    # condition
    # if word in word_frequencies:
        # already exists, therefore, increment the value
        # word_frequencies[word] += 1
    # else:
    #     # Initialize
    #     word_frequencies[word] = 1
# print(word_frequencies)

mydictionary = {
    "name": "Hezron",
    "age": 23,
    "city": "Nairobi"
}

# for key, value in mydictionary.items():
#     print(f"{key} {value}")

"""
    In summary : List, Dictionary, Tuples, Sets, => How to access, there methods, Loop through, Check whether element exist, 
"""
# Sets: Unorder, Mutable, No Duplicate
# e.g 
odds = {1, 3, 5, 7, 9}
evens =  {0, 2, 4, 6, 6, 8}
primes = {2, 3, 5, 7}

# Union => adds both sets with No duplication
u = odds.union(evens)
# print(u) 

# Intersection
i = odds.intersection(primes)
# print(i)

# .isesubset, 


"""
    String: order, Immutable, text representation.
    1. Loop
    2. sep => default is a space, therefore, when use sep="wil" , it will output what your have specificed
    3.  end
    4. Methods :=> strip(), startswith(), lower()
"""
# Union and interset
# greetings = "Hello"
# for x in greetings:
#     if 'e'  in x:
        # print("It's available", sep="", end="")
# from timeit import default_timer as timer

# my_list = ['a'] * 6
# # print(my_list)

# # bad
# start = timer()
# my_string = ''
# for i in my_string:
#     my_string += i
# stop = timer()
# print(stop - start)

# # good
# start = timer()
# my_string = ''.join(my_list)
# print(my_string)
# stop = timer()
# print(stop - start)


"""
    % => placeholder, .format(), f-String
"""

var = "Hezron"
var2 = 6
# %s => string
# %d => integer
# %.2f => float
my_string = "the variable is %s" %var

my_string = "the variable is {} and {}".format(var, var2)



"""
    Collections : Counter, namedtuple, orderedDict, defaultdict, deque
"""

# Counter

from collections import Counter

a = "aaaaaabbbbbcccc"
# Counter returns Dictionary
my_counter = Counter(a)
# print(my_counter.items())


# Deque
from collections import deque

d = deque()

d.append(1)
d.append(2)

d.appendleft(3)
# print(d)


d.extendleft([4, 5, 6])

# print(d)

"""
    Itertools:=> it's module tools for handling iitertors, are data types that can be used in a for loop. 
    ITERTOOLS OFFERS ADVANCED TOOLS SUCH AS:-
        1. Product => return a list
        2. Permutatuions => return all possible ordering of an input
        3. Combinations
        4. Acculate
        5. Groupby
        6. Infinite iterators
"""

from itertools import product, permutations, groupby

a = [1, 2]
b = [3, 4, 5, 6]

prod = product(a,b)
# print(list(prod))

x = [3, 4, 6]
perm = permutations(x)
print(list(perm))

def small_than_3(x):
    return x < 3

a = [1, 2, 3, 4, 5]
group_obj = groupby(a, key=small_than_3)

for key, value in group_obj:
    print(key, list(value))


person = [
    {'name': 'Tim', 'age': 24},
    {'name': 'Hezron', 'age': 24},
    {'name': 'Allan', 'age': 30},
]

grp_obj = groupby(person, key=lambda x: x['age'])
for key, value in grp_obj:
    print(key, list(value))


"""
    LAMBDA => Is a small one line anonymous function that is define without a name.

    SYNTAX:
    lambda parameter: expression
"""
add10 = lambda x: x + 10

print(add10(5))

# OR::

def add10_func(x):
    return x + 10

points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D, key=lambda x: x[1])


# map(func, seq)
# filter(func, seq) => returns true or false
a = [1, 2, 3]
b = map(lambda x: x*2, a)
print(list(b))

# list compression
c = [x*2 for x in a]
# print(c)

# filter
# c = filter(x for x in a if x%2==0)

# reduce(func, seq)
from functools import reduce
prod_a = reduce(lambda x, y: x*y , a)

# print(prod_a)


"""
    Exceptions :=> Python terminate as soon as encouters an error / exceptions.

    Difference btn syntax error and exception?
    1. TypeError
    2. ModuleNotFound
    3. ValueError
    4. IndexError
    5. KeyError
    6. ZeroDivisionError

    NOTE : Understand the possible errors.
"""

# syntax e.g
# a = 5 + '10'
# output => TypeError ~> unsupported operand type

""" import somemodule """

# Output : ModuleNotFoundError: No module named 'somemodule'

# #  Custom raise Exception
# x = -5
# if x < 0:
#     raise Exception('X Should Be Positive')

# Can use  Assert

x = -5
assert ( x >= 0), 'X is not positive'


try:
    a = 5 / 1
    b = a + 4
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('Everything is fine')
finally:
    print('ckeaning Up ...')