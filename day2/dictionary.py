"""
Dictionary / HashMap / Map
f : integer --> anything
    index: key --> value: anything

dictionary
key: anything --> value: anything
(unique)          not unique

{}
"""

words = {
    'i': 100,
    'am': 20,
    'batman': 87
}

print(type(words))

print(words['batman'])
words['batman'] = 100
print(words['batman'])

print(words)
words['hello'] = 1
print(words)

# removing value from dictionary
del words['hello']
print(words)

keys = words.keys()
print(keys)
print(type(keys))

values = words.values()
print(values)
print(type(values))

items = words.items()
print(items)
print(type(items))

# iterating over dict
print('\n\n\n')

# for key in words.keys(): # same as --> in words
#     print(key)

# for value in words.values():
#     print(value)

# for item in words.items():
#     key = item[0]
#     value = item[1]
#     print(key + ' - ' + str(value))


for key, value in words.items():
    print(key + '  -  ' + str(value))
