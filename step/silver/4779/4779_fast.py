import sys

k = "-"

# N 범위가 정해져있음
for _ in range(12):
    k = k + " " * len(k) + k

for line in sys.stdin:
    n = int(line.strip())
    N = 3**n
    print(k[:N])
