""""
Map operator
map(func, iterable)

iterable: i1, i2, i3, i4 ..... in
iterable: func(i1) func(i2) func(i3) func(i4) ....
"""

numbers = list(map(int, input().split(' ')))
print(type(numbers))
print(numbers)
