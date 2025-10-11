# 문제
# 양수 A가 N의 진짜 약수가 되려면, N이 A의 배수이고, A가 1과 N이 아니어야 한다.
# 어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N의 진짜 약수의 개수가 주어진다. 이 개수는 50보다 작거나 같은 자연수이다.
# 둘째 줄에는 N의 진짜 약수가 주어진다.
# 1,000,000보다 작거나 같고, 2보다 크거나 같은 자연수이고, 중복되지 않는다.


# 문제는 약수들의 최소 공배수 but 약수를 포함하지 않는 최소 공배수를 원함.
# ex) 3,4,12 가 있으면, 12가 아닌 24를 원함
# 결론 : 약수들의 최소 공배수를 찾고, max(약수) 와 같으면 x 가장 작은 약수 (진짜 약수가 "모두" 주어지기 때문에)
# 핵심 : 여러개의 숫자의 최소 공배수를 빠르게 구하는 방법


import sys

input = sys.stdin.readline


def LCM(arr):
    # 리스트를 받아서 최소 공배수를 구하는 함수
    re = 1
    while len(arr) != 0:
        divider = min(arr)
        count_1 = 0
        for i in range(len(arr)):
            if arr[i] % divider == 0:
                arr[i] //= divider
                if arr[i] == 1:
                    count_1 += 1

        for _ in range(count_1):
            arr.remove(1)
        re *= divider
    return re


N = int(input())

num_list = list(map(int, input().split()))
max_num = max(num_list)
min_num = min(num_list)
lcm = LCM(num_list)

result = lcm * min_num if lcm == max_num else lcm

print(result)
