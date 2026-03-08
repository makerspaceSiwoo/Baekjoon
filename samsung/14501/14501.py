import sys

input = sys.stdin.readline

N = int(input())

table = {}

def profit(max_profits, table, day, last_day):
    t,p = table[day]
    if day + t > last_day:
        max_profits[day] = p
    else:
        max = 0
        for key, value in max_profits.items():
            if key >= day + t:
                max = value if value > max else max
        max_profits[day] = max + p


for i in range(1,N+1):
    t,p = list(map(int, input().split()))
    if i + t > N + 1 :
        continue
    else:
        table[i] = [t,p]

max_profits = {}

if len(table.keys()) == 0:
    print(0)
    exit()
else: 
    last_day = max(table.keys())
    for day in reversed(table.keys()):
        profit(max_profits, table, day, last_day)

    print(max(max_profits.values()))