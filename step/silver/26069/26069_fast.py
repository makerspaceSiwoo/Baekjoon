import sys

input = sys.stdin.readline

n = int(input())

result = {"ChongChong"}

for i in range(n):
    a, b = input().split()

    if a in result:
        result.add(b)

    if b in result:
        result.add(a)

print(len(result))
