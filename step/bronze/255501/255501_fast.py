import sys
import os

input = sys.stdin.readline

N = int(input())

for i in range(N):
    word = input().strip()

    reversed = word[::-1]

    if word == reversed:
        print(1, len(word) // 2 + 1)
    else:
        prefix = os.path.commonprefix(
            [word, reversed]
        )  # 공통 접두사를 알려주는 os 함수
        print(0, len(prefix) + 1)
