import sys

input = sys.stdin.readline

n, k = map(int, input().split())

round = [i for i in range(1, n + 1)]

result = []
target = 0

while len(round) > 0:
    target = (target + (k - 1)) % len(round)
    # pop 을 사용하면, 리스트 중간 원소를 pop 하면서 뒤 내용을 당기므로 시간 복잡도가 O(n^2)이 된다.
    result.append(round.pop(target))

print("<" + ", ".join(map(str, result)) + ">")
