import sys

input = sys.stdin.readline
write = sys.stdout.write

n = int(input())


def hanoi(n, a, b, c):
    if n == 1:
        move = "{} {}".format(a, c)
        return [move]

    key = (n, a, b, c)
    if key in memo:
        return memo[key]

    result = []
    prev = hanoi(n - 1, a, c, b)
    result.extend(prev)
    move = "{} {}".format(a, c)
    result.append(move)
    next = hanoi(n - 1, b, a, c)
    result.extend(next)

    memo[key] = result
    return result


memo = dict()
result = hanoi(n, 1, 2, 3)
write(str(len(result)) + "\n")
write("\n".join(result))
