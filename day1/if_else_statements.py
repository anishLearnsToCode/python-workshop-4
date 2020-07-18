"""
If else

predicate = is any logical expression

if predicate:
    code
elif predicate2: (not compulsory)
    code2
elif predicate3:
    code3
..
..
..
..
else: (not compulsory)
    code
"""

# switch statements not supported by python
number = int(input())

if number > 10:
    print('i am in if block')
    print('still here')
    print('still in if block')
elif number > 0:
    print('number greater than 0')
elif number > -10:
    print('very small number')
elif number > -10000:
    print('extremely small number')
else:
    print('what kind of number is this !!!!!!!')

# if number > 10:
#     print(number)
#     print(number + 100)
#     print(number / 10)
#
# if number > 0:
#     print(number)
#
# if number > -100:
#     print(number)

print('i am outside if else')
