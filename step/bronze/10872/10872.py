import sys

input = sys.stdin.readline

N = int(input())

re = 1
for i in range(1, N + 1):
    re *= i

print(re)
