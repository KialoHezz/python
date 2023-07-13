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
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    
    return wrapper


@start_end_decorator
def add(x):
    return x + 5

add(10)