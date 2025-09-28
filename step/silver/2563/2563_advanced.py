import sys

input = sys.stdin.readline

area = [[0] * 100 for _ in range(100)]

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    for j in range(x, x + 10):
        for k in range(y, y + 10):
            area[j][k] = 1

result = 0

for row in area:
    result += sum(row)  # 리스트 내에서 합 함수를 사용할 수 있다.

print(result)
