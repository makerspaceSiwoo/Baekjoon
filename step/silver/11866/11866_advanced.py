import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

round = deque(range(1, n + 1))

result = []

while round:
    round.rotate(-(k - 1))
    result.append(round.popleft())

print(f"<{', '.join(map(str, result))}>")
