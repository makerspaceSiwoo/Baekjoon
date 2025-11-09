import sys
from functools import lru_cache

input = sys.stdin.readline


# 길이가 N인 merge_sort 시 저장 횟수 (n이 2 이상일 때만 성립)
@lru_cache(maxsize=None)  # 재귀 함수의 캐싱으로 재사용하기
def N_saves(n: int):
    if n < 2:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 5
    else:
        left = N_saves((n + 1) // 2)
        right = N_saves(n - ((n + 1) // 2))
        return left + right + n


# 문제에서 주어진 함수의 k 번째 저장된 수를 구하는 함수
def K_save(arr: list, k: int, start: int, end: int):
    N = end - start
    if N == 1:
        if k > 1:
            return -1
        else:
            return arr[0]
    elif k > N_saves(N):
        return -1
    elif N <= 2:
        sorted_arr = sorted(arr[start:end])
        return sorted_arr[k - 1]
    else:
        left = (N + 1) // 2
        right = N - left
        N_left = N_saves(left)
        N_right = N_saves(right)
        if k > N_left + N_right:
            sorted_arr = sorted(arr[start:end])
            return sorted_arr[(k - (N_left + N_right)) - 1]
        elif k > N_left:
            new_k = k - N_left
            return K_save(arr, new_k, start + left, end)
        else:
            return K_save(arr, k, start, start + left)


n, k = map(int, input().split())
arr = list(map(int, input().split()))

print(K_save(arr, k, 0, n))
