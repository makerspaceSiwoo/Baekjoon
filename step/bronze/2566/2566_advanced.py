import sys

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

max_val = 0
pos = (1,1)

for i, row in enumerate(matrix):
    for j, val in enumerate(row):
        if val > max_val:
            max_val = val
            pos = (i + 1, j + 1)

print(max_val)
print(*pos)