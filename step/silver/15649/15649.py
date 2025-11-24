import sys

input = sys.stdin.readline
write = sys.stdout.write

N, M = map(int, input().split())

used = {i: False for i in range(1, N + 1)}

result = []


def func(used, n, m, str):
    if m > 0:
        for i in range(1, n + 1):
            if not used[i]:
                used[i] = True
                new_str = str + " {}".format(i)
                func(used, n, m - 1, new_str)
                used[i] = False
            else:
                continue
    else:  # m == 1
        result.append(str.lstrip())
        last = str[-1]
        used[last] = False


func(used, N, M, "")

write("\n".join(result))
