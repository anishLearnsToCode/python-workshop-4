numbers = input().split(' ')

for index in range(len(numbers)):
    numbers[index] = int(numbers[index])
    print(numbers)

print(type(numbers))
