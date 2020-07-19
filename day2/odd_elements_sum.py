def sumOddNumbers(n):
    return sum(2 * number + 1 for number in range(n))


print(sumOddNumbers(10))
