import sys

input = sys.stdin.readline

N, K = map(int,input().split())

multap = [0] * N

li = list(map(int,input().split()))

# res 바꾼 횟수, swap 변경할 리스트 넘버, num 어디부터 바꾸는지, max_I 모두 안에 있을 때 마지막 값.
res = swap = num = max_I = 0

for i in li:
    # 있으면 패스
    if i in multap:
        pass
    # 멀티탭에 0이 있으면 그 자리에 연결
    elif 0 in multap:
        multap[multap.index(0)] = i
    else:
        # 멀티탭 안에 있는 거 확인
        for j in multap:
            # 멀티탭 안에 있는 것이 나머지 리스트에 없을 경우
            if j not in li[num:]:
                # 그것을 swap에 확인한다.
                swap = j
                break
            # 멀티탭 안에 있는 것들이 모두 나머지에 있다면
            # 마지막 있는 것을 swap으로 정함.
            elif li[num:].index(j) > max_I:
                max_I = li[num:].index(j)
                swap = j
        # 마지막에 있는 것을 i로 정하고
        multap[multap.index(swap)] = i
        # max 값하고 swap 값 초기화
        max_I = swap = 0
        # 바꾼 횟수 카운트
        res += 1
    # num의 오른쪽 부터 남은 부분.
    num +=1
print(res) 