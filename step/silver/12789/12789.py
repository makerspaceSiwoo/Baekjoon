import sys

N = int(sys.stdin.readline().rstrip())

queue = list(map(int, sys.stdin.readline().split()))

stack = []

next = 1

possible = True

while next < N:
    if len(queue) == 0 and stack[-1] != next:
        possible = False
        break
    elif len(queue) != 0 and queue[0] == next:
        queue.pop(0)
        next += 1
        continue
    elif len(stack) != 0 and stack[-1] == next:
        stack.pop()
        next += 1
        continue
    else:
        item = queue.pop(0)
        stack.append(item)
        continue

if possible:
    print("Nice")
else:
    print("Sad")
