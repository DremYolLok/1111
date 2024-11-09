# A

try:
    func()
except (SystemError, ValueError, TypeError) as error:
    print(type(error).__name__)
else:
    print('No Exceptions')

# B

func('1', None)

# C

class A:

    def __init__(self):
        pass

    def __str__(self):
        raise Exception()    
        
    def __repr__(self):
        raise Exception()  


func(A())

# D

def only_positive_even_sum(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError
    if not (a > 0 and not a % 2) or not (b > 0 and not b % 2):
        raise ValueError
    return a + b

# E

def merge(iterable1, iterable2):
    try:
        iterator1 = iter(iterable1)
        iterator2 = iter(iterable2)
    except TypeError:
        raise StopIteration
    if any(not isinstance(element, type(iterable1[0])) for element in iterable1):
        raise TypeError
    if any(not isinstance(element, type(iterable1[0])) for element in iterable2):
        raise TypeError
    if list(iterable1) != sorted(iterable1) or list(iterable2) != sorted(iterable2):
        raise ValueError
    return tuple(sorted(list(iterable1) + list(iterable2)))
