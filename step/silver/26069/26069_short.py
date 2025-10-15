d = {"Chong" * 2}

for i in open(0):  # 파일처럼 입력 받음
    i = {*i.split()}  # 두명 분리
    if d & i:  # 교집합 있으면
        d |= i  # 합집합에 추가

print(len(d))
