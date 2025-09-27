import sys

n, m = map(int, sys.stdin.readline().split())

A = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
B = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

result = [(x+y for x,y in zip(a,b)) for a, b in zip(A,B)] # zip : 배열 내 요소를 병렬로 처리 가능

for i in range(len(result)):
    print(*result[i])