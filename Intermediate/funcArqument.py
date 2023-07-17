"""
    - The difference btn arquments and parameters
    - Positional and keyword arquments
    - Default arquments
    - Variable-Length arquments
    - Container unpacking into function arquments
    -  local Vs.  global arquments
    - Parameter passing (by value or by reference?)
"""
# name => parameter 
def print_name(name):
    print(name)
# call function
# Hezron => arqument
print_name('Hezron')


def foo(a, b, c):
    print(a, b, c)
# positional arqument
foo(1, 2, 3)
# keyword arqument
foo(c=1, a=2, b=3)

   
# - Variable-Length arquments [args=> position arquments, kwargs=> keyword arqument]
def fool(a, b, *args, **kwargs):
    print(a, b)

    for arg in args:
        print(arg)
    
    for key in kwargs:
        print(key, kwargs[key])

fool(1, 2, 3, 4, 5, six=6, seven=7)
# unpacking arquments

def fo(a, b, c):
    print(a, b, c)

# list    Tuple
my_list = (0, 1, 2)
fo(*my_list)

# dictionary
my_dict = {'a': 1, 'b':3, 'c':8}
fo(**my_dict)
 