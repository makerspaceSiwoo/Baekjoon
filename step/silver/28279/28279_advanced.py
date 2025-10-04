from collections import deque


def main():
    data = open(0).read().split()  # 입력 전체를 한 번에 읽기
    n = int(data[0])
    dq = deque()
    out = []  # 출력 결과를 저장할 리스트
    i = 1  # 현재 인덱스

    for _ in range(n):
        cmd = int(data[i])
        i += 1

        if cmd == 1:
            dq.appendleft(int(data[i]))
            i += 1
        elif cmd == 2:
            dq.append(int(data[i]))
            i += 1
        elif cmd == 3:
            out.append(str(dq.popleft()) if dq else "-1")
        elif cmd == 4:
            out.append(str(dq.pop()) if dq else "-1")
        elif cmd == 5:
            out.append(str(len(dq)))
        elif cmd == 6:
            out.append("0" if dq else "1")
        elif cmd == 7:
            out.append(str(dq[0]) if dq else "-1")
        elif cmd == 8:
            out.append(str(dq[-1]) if dq else "-1")

    print("\n".join(out))  # 한 번에 출력


if __name__ == "__main__":
    main()
