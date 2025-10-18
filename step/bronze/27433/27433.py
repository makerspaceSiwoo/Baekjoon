# n factorial

# 반복문
import sys
from functools import reduce

N = int(sys.stdin.readline())

# 반복문 1st
if N == 0:
    print(1)
else:
    acc = 1
    for y in range(1, N + 1):
        acc = (lambda x, y: x * y)(acc, y)
    print(acc)

# reduce, lambda 3rd
if N == 0:
    print(1)
else:
    print(reduce(lambda x, y: x * y, range(1, N + 1)))


# 재귀 2nd
def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n


print(factorial(N))
