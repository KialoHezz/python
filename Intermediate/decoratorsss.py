import functools
"""
    1. Concept Behind the decorators
    2. Difference between class and function decorators
"""

# function decorators
# decorator syntax look
"""
    Function in python a first class object => means they can be dfn inside other objects
"""
# Function Identities
def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    
    return wrapper


@start_end_decorator
def add(x):
    return x + 5

# print(help(add()))
# print(add.__name__)

# Example of decorators function 

def repeat(num_time):
    def decorator_repeat(fun):

        @functools.wraps(fun)
        def wrapper(*args, **kwargs):
            for _ in range(num_time):
                result = fun(*args, **kwargs)

            return result
        return wrapper
    return decorator_repeat

# decorator
@repeat(num_time=20)
# dfn a function greating with parameter name of the person
def greet(name):
    print(f'Hello {name}!')

# call the function
greet('Allan')





