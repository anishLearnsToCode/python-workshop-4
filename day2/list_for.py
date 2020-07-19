numbers = [2, 3, 5, 7, 11, 13, 17, ['hello', 'world'], range(5)]


def sumInList(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

# for number in numbers:
#     print(number)


print(sumInList([1, 2, 3]))
print(sumInList([-1, -100, 34, 56, 100]))
