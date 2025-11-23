import sys

# sys.setrecursionlimit(10**7)  # 파이썬 기본 재귀 제한 해제 - 이 문제에서는 필요 없음

write = sys.stdout.write


def draw_star(n):
    if n == 1:
        return ["*"]

    prev = draw_star(n // 3)
    arr = []

    for line in prev:
        arr.append(line + line + line)

    blank = " " * (n // 3)

    for line in prev:
        arr.append(line + blank + line)

    for line in prev:
        arr.append(line + line + line)

    return arr


N = int(sys.stdin.readline())
pattern = draw_star(N)
write("\n".join(pattern))
