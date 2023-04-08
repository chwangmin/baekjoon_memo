import sys

num = int(sys.stdin.readline())

# 1, 2 ,3 번 받침대가 있으니까 보조 받침대를 6-start-end 로 계산
# no-1번을 먼저 보조 받침대로 이동하기.

def hanoi(no, start, end):
    if no > 1:
        # 먼저 시작 포인트에서 보조 포인트로 이동.
        hanoi(no-1, start,6-start-end )
    print(start, end)
    if no > 1:
        # 마지막으로 보조에서 끝 포인트로
        hanoi(no-1, 6-start-end, end)

print(2 ** num - 1)
if num <= 20:
    hanoi(num,1,3)