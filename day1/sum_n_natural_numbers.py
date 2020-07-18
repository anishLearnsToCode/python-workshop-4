"""
N
1 + 2 + 3 + ... + N
"""

n = int(input())

# efficient code
# print(n * (n + 1) / 2)

# i = 0
# sum = 0
# while i <= n:
#     sum += i
#     i += 1

sum = 0
for i in range(1, n + 1):
    sum += i

print(sum)
