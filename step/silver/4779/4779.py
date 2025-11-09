import sys


def funcA(arr: list, start: int, end: int):
    if start >= end - 1:
        return

    i = (end - start) // 3
    j = start + i
    k = j + i

    for x in range(j, k):
        arr[x] = 0

    funcA(arr, start, j)
    funcA(arr, k, end)


def get_arr(n: int):
    return [1 for _ in range(3**n)]


def funcB(n: int):
    arr = get_arr(n)
    funcA(arr, 0, len(arr))
    result = ""
    for i in arr:
        if i == 1:
            result += "-"
        else:
            result += " "
    print(result)


for line in sys.stdin:
    N = int(line.strip())
    funcB(N)
