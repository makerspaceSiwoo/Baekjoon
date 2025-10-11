# 속도 개선을 위해, 입출력을 한 번에 처리함

import sys

logs = iter(sys.stdin.read().split("ENTER"))

print(sum(len(set(log.split())) for log in logs) - 1)  # 처음 들어간 숫자 제외
