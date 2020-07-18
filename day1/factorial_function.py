def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result


def permutation(n, r): # nPr = n! / (n - r)!
    return factorial(n) / factorial(n - r)
    # factorial(4) / factorial(4)
    # 24.0 / factorial(4)
    # 24.0 / 24.0
    # 1.0
    # return 1 --->


def combination(n, r): # nCr n! / r! * (n - r)! = nPr / r!
    return permutation(n, r) / factorial(r)
    # return 1.0 / factorial(0)
    # return 1.0 / 1
    # return 1.0 / 1.0
    # return 1.0
    # ---> 1.0


# f o g (x) f(g(x))
# print(combination(4, 0))
# # print(1.0)
#
# print(combination(4, 1))
# print(combination(4, 2))
# print(combination(4, 3))
# print(combination(4, 4))

n = int(input())
r = int(input())

print(permutation(n, r))
