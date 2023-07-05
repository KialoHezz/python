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

# person_name = input("What's your name? ")
# favourite_color = input("What color do you like? ")

# use print() and + to concantinate
# print(person_name + "likes" + favourite_color)

"""
    3rd Question: 
    Ask a user their weight(in pounds), convert it kilograms and print on the terminal.
   
"""

# Thought process / Pseoudocode 

# user_weight = float(input("What's you weigth lbs: "))
# weight_kg = user_weight  * 0.45

# print(weight_kg)

"""
    Guessing Game
"""

secret_number = 9
# represent the no. of user guesses

guess_count = 0
# user should guess three times
guess_limit = 3

# while guess_count < guess_limit:
#     guess = int(input('Take a Guess: '))
#     guess_count += 1

#     if guess == secret_number:
#         print("You Won")
#         # terminate
#         break
# else:
#     print("Sorry you failed")


"""
    Car Game : 1. start => Car started
               2. stop => car Stoped
               3. quit => terminates the loop
"""
# # dry => dont repeat yourself
# command = ""
# started = False
# while True:
#     command = input(">").lower()
#     if command == 'start':
#         if started:
#             print("car already started")
#         else:
#             started = True
#         print("Car started ...")
#     elif command == 'stopped':
#         if not started:
#             print("Car already stopped")
#         else:
#             started = False
#         print("Car Stopped")

#     elif command == "help":
#         print("""
# start - to start the car
# stop - to stop the car
# quit - to quit
#         """)
#     elif command == 'quit':
#         break
    
#     else:
#         print("sorry I don't understand that")

"""
    write a program to find the largest number in a list
"""

numbers = [1, 20, 3, 40, 50]

max = numbers[0]

for number in numbers:
    if number > max:
        max = number
print(max)