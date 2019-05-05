"""
Variable length argument and keyword argument for function parameter list

Called function does not know how many arguments caller will passed in.
"""


def add(a, b=-2, *args, **kwargs):
    total = a
    for val in args:
        total += val
        
    for key in kwargs:
        total += kwargs[key]
        
    return total


# print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
'''
1
1
4
'''

myarg = range(10)
print(add(*myarg))
'''
44
'''

mydict = {
    # 'b': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    }

print(add(2, *myarg, **mydict))
'''
32
'''
