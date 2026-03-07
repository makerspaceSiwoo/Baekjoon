import sys

input = sys.stdin.readline

N = int(input())

students = list(map(int, input().split()))

B, C = map(int, input().split())

result = N  # N 총감독은 모든 시험장에 있어야 함.
for a in students:
    if a <= B:  # 오답 노트 : a 가 B 보다 작을 수 있다는 경우를 생각하지 못함
        continue
    result += ((a - B) + C - 1) // C # 총감독이 감시할 수 있는 사람의 수를 제외한 나머지 중, 필요한 부감독 수를 구함

print(result)