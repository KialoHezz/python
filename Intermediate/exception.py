class valueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise valueTooHighError('Value is too High')
    if x < 5:
        raise ValueTooSmallError('Value Tooo Small', x)
    
try:
    test_value(1)
except valueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)