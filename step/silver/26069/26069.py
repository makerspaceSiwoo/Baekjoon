# 첫번째 줄에는 사람들이 만난 기록의 수
# $N\ (1 \le N \le 1\ 000)$이 주어진다.

# 두번째 줄부터
# $N$개의 줄에 걸쳐 사람들이 만난 기록이 주어진다.
# $i + 1$번째 줄에는
# $i$번째로 만난 사람들의 이름
# $A_i$와
# $B_i$가 공백을 사이에 두고 주어진다.
# $A_i$와
# $B_i$는 숫자와 영문 대소문자로 이루어진 최대 길이
# $20$의 문자열이며, 서로 같지 않다.

# 총총이의 이름은 ChongChong으로 주어지며, 기록에서 1회 이상 주어진다.

# 동명이인은 없으며, 사람의 이름은 대소문자를 구분한다.
# (ChongChong과 chongchong은 다른 이름이다.)


# 문제의 핵심?
# ChongChong 이 나온 순간부터 무지개 댄스 세트를 만들고,
# 입력 조합에서 무지개 댄스 세트에 있으면, 같이 나온 사람을 추가한다.
# 성능 최적화는 I/O bound

import sys

target = "ChongChong"

logs = sys.stdin.read().split("\n")  # 각 줄

meet = [log.split() for log in logs]  # 각 줄 만난 사람 둘을 리스트로

result = set([target])  # ChongChong 과 만난 사람 세트 (중복 제거)

# 세트와 만남 교집합을 통해서, 있으면 세트에 추가 - 내 생각에는 이게 빠를 줄 알았는데,
# for m in meet:
#     if result & set(m):
#         result.update(m)

# 교집합 연산, update 연산보다 아래가 빠름
for m in meet:
    if len(m) != 2:
        continue
    if m[0] in result:
        result.add(m[1])
    if m[1] in result:
        result.add(m[0])

print(len(result))
