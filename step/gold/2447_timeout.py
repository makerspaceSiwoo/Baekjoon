import sys

input = sys.stdin.readline

N = int(input().strip())

k = int(N ** (1 / 3))

write = sys.stdout.write

matrix = []


def is_blank(x, y, N):
    while N > 0:
        start = N // 3
        end = start * 2 + 1
        a = x % N
        b = y % N
        if start < a and a < end and start < b and b < end:
            return True
        N //= 3
    return False


for y in range(N):
    line = []
    for x in range(N):
        line.append(" " if is_blank(x + 1, y + 1, N) else "*")
    write("".join(line) + "\n")
