import sys

input = sys.stdin.readline

def sol(num,start,end):
    if num==0:
        return
    cnt = end // 3


while(True):
    try:
        num = int(input())
        answer = ['-'] * (3**num)
        sol(num,0,num**3-1)
        print(''.join(answer))
    except:
        break