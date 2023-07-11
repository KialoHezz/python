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
print(i)

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

