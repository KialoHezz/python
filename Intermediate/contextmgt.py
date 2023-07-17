class ManagedFile:
    def __init__(self, filename):
        print('init')
        self.filename = filename

    def __enter__(self):
        print('Enter')
        self.file = open(self.filename, 'w')

        return self.file


    def __exit__(self, exc_type, exec_value, exec_traceback):
        if self.file:
            self.file.close()
            print('exit')



with ManagedFile('notes.tx') as file:
    print('do some stuff')
    file.write('some to doo')



#  Generators, context manager & Decorator

from contextlib import contextmanager


@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w')

    try:
        yield f
    finally:
        f.close()

with open_managed_file('notes.txt') as f:
    f.write('some todoo...')

    
