import sys

input = sys.stdin.readline

n = int(input())
waitList = list(map(int, input().split()))

stack = []

next = 1

for i in range(n):
    stack.append(i)
    while stack and stack[-1] == next:
        stack.pop()
        if len(stack) > 1 and stack[-1] > stack[-2]:
            print("Sad")
            sys.exit()

if stack:
    print("Sad")
else:
    print("Nice")
