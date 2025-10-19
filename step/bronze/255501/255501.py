# def recursion(s, l, r):
#     if l >= r: return 1
#     elif s[l] != s[r]: return 0
#     else: return recursion(s, l+1, r-1)

# def isPalindrome(s):
#     return recursion(s, 0, len(s)-1)

# print('ABBA:', isPalindrome('ABBA'))
# print('ABC:', isPalindrome('ABC'))
# 문제 : 함수의 반환값과 recursion 함수의 호출 횟수를 구해보자.

import sys

input = sys.stdin.readline

N = int(input())


def recursion(s, l, r, cnt):
    cnt += 1
    if l >= r:
        return (1, cnt)
    elif s[l] != s[r]:
        return (0, cnt)
    else:
        return recursion(s, l + 1, r - 1, cnt)


def isPalindrome(s, cnt):
    return recursion(s, 0, len(s) - 1, cnt)


for i in range(N):
    word = input().strip()
    print(*(isPalindrome(word, 0)))
