import sys

input = sys.stdin.readline
write = sys.stdout.write

N, M = map(int, input().split())


result = []


def func(used, n, m, str):
    if m > 0:
        if used + 1 >= n + 1:
            return
        for i in range(used + 1, n + 1):
            new_str = str + " {}".format(i)
            func(i, n, m - 1, new_str)
    else:
        result.append(str.lstrip())


func(0, N, M, "")

write("\n".join(result))
