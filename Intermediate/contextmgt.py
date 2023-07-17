"""# Are great tool for resource mgt , they allow you to allocate and release resource precisely when you want to.
    1. Context manager in what are used for,
    2. typical examples of context manager,
    3. How to implement our context manager
"""

file = open('notes.txt', 'w')

try:
    file.write('some to doo..')
finally:
    file.close()

# OR


# context manager
with open('notes.txt', 'w') as file:
    file.write('some todoo..')


from threading import Lock

lock = Lock()

lock.acquire()
# ...
lock.release()

# OR

# context manager
with lock:
    pass
