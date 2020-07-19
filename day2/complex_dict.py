"""
not allowed as keys:
dict
lists

boolean --> treated as int internally
"""

complex = {
    'hello': 'world ----',
    range(1, 10, 2): range(1, 5, 3),
    'list': [2, 5, 7],
    34: [1, 2, 3, 4, 5, 6],
    1: 100,
    'awesome': {
        'pi': 3.14,
        'e': 2.71828,
        'hi there': [
            1,
            'hello',
            {
                'nested': 'omg!!!!'
            }
        ]
    },
    5.00008: 'hi there'
}

# print(complex['awesome']['hi there'][2]['nested'])
# print(complex.get('hello'))

# check whether key present in dict or not
print(20 in complex)

print(complex)
complex.clear()
print(complex)
