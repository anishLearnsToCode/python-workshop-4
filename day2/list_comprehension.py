"""
{1, 4,9, 16 ....}
{x ^ 2 | x in (1, 10)}
{x + 5 | 0<= x <= 20 }

f(var) for var in range()
lists are iterable
"""


def isEven(number):
    return number % 2 == 0


numbers = [x for x in range(1, 11)]
print(numbers)

squares = [x ** 2 for x in range(1, 11)]
print(squares)

funky = [number if isEven(number) else '*' for number in range(1, 20)]
print(funky)
