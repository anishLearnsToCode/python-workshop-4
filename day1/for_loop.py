"""
For loop

for variable in iterable_object:
    code

iterable objects
- string
- range
"""

# for i in range(5, 10):
#     print(i)

# for i in range(10, 1, -2):
#     print(i)

# for character in 'hello world':
#     print(character)

for i in range(1, 5):
    for j in range(10):
        print(str(i) + ' * ' + str(j) + ' = ' + str(i * j))
    print()
