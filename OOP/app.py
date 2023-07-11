"""
    Object Orienttated Programming in Python
    
"""
# Everything that we do in python is actually an object of some kind of class 
print(type("Hello"))

# blueprint
class Dog:

    # method are dfn inside the class
    def bark(self):
        print("bark")
# Instance
d = Dog()
print(type(d))