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
user_input = input("write your sentence: ")

# split the words => split method returns a array
words = user_input.split(" ")

# dictionary
word_frequencies = {}
# iterate the array
for word in words:
    # condition
    if word in word_frequencies:
        # already exists, therefore, increment the value
        word_frequencies[word] += 1
    else:
        # Initialize
        word_frequencies[word] = 1
print(word_frequencies)

