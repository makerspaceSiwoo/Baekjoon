import sys

input = sys.stdin.readline

N = int(input())

result = 0

nick_name = set()

for _ in range(N):
    word = input().rstrip()

    if word == "ENTER":
        result += len(nick_name)
        nick_name = set()  # 리셋
    else:
        nick_name.add(word)

if len(nick_name):
    result += len(nick_name)

print(result)
