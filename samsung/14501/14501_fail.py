import sys

input = sys.stdin.readline

N = int(input())

table = {}

# 예외 - 가능한 날짜가 없는 경우를 고려하지 않음. ex) 1 : 4,9
for i in range(1,N+1):
    t,p = list(map(int, input().split()))
    if i + t > N + 1 :
        continue
    else:
        table[i] = [t,p]

max_profits = {}

last_day = max(table.keys())

def profit(max_profits, table, day):
    t,p = table[day]
    # if day + t not in max_profits.keys(): 
    # 이 경우, day + t 는 max_profits에 없을 수 있지만, 선택 가능한 날짜가 존재할 수 있음
    # if day + t > table.keys()[-1]: # TypeError: 'dict_keys' object is not subscriptable
    if day + t > last_day:
        max_profits[day] = p
    else:
        max = 0
        for key, value in max_profits.items():
            if key >= day + t:
                max = value if value > max else max
        max_profits[day] = max + p

for day in reversed(table.keys()):
    profit(max_profits, table, day)


print(max(max_profits.values()))