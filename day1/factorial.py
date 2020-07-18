"""
N
1 * 2 * 3 * ... * N
0! = 1
"""

n = int(input())

# f = 1
# while n > 0:
#     f = f * n
#     n -= 1

result = 1
for i in range(1, n + 1):
    result *= i

print(result)
