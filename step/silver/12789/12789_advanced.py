import sys

N = int(sys.stdin.readline().rstrip())

queue = list(map(int, sys.stdin.readline().split()))

next = 1

possible = True

# next 의 요소의 왼쪽을 stack 으로 간주, 해당 stack 가 내림차순이 아니라면, 오류

for i in range(1, N):
    index = queue.index(i)
    stack = queue[:index]
    copy = stack[:]
    stack.sort(reverse=True)
    if copy != stack:
        possible = False
        break
    else:
        queue.pop(index)
        next += 1
        continue

if possible:
    print("Nice")
else:
    print("Sad")
