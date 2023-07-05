"""
    1. We Check In a patient named John Kyalo. He's 20 yrs old and is a new patient
"""

# dfn variable
name = 'John Kyalo'
age = 20
is_new = True

"""
    Ask two question: person's name and favourite color. Then, print a message like 'Hezron likes blue'
"""

# Thought process // Pseudocode 1. use input function to get user  input and print function to output the result

person_name = input("What's your name? ")
favourite_color = input("What color do you like? ")

# use print() and + to concantinate
# print(person_name + "likes" + favourite_color)

"""
    3rd Question: 
    Ask a user their weight(in pounds), convert it kilograms and print on the terminal.
   
"""

# Thought process / Pseoudocode 

user_weight = float(input("What's you weigth lbs: "))
weight_kg = user_weight  * 0.45

print(weight_kg)