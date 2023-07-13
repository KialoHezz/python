"""
    1. Concept Behind the decorators
    2. Difference between class and function decorators
"""

# function decorators
# decorator syntax look
"""
    Function in python a first class object => means they can be dfn inside other objects
"""
def start_end_decorator(func):
    def wrapper():
        print('Start')
        func()
        print('End')
    return wrapper


@start_end_decorator
def print_name():
    print('Hezron')

print_name()