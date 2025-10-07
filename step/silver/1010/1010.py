import sys

input = sys.stdin.readline

T = int(input())


def permulation(a, b):
    re = 1
    for i in range(b):
        re *= a - i
    return re


def combination(a, b):
    if b >= (a // 2 + 1):
        return combination(a, a - b)
    else:
        return permulation(a, b) // permulation(b, b)


for i in range(T):
    n, m = map(int, input().split())
    print(combination(m, n))
