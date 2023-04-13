import sys

def back_tracking(idx, res):
    global cnt

    if idx >= n:
        return
    
    res += k[idx]

    if res == s:
        cnt+=1

    back_tracking(idx + 1, res)
    back_tracking(idx + 1, res - k[idx])


n, s = map(int, sys.stdin.readline().split())
k = list(map(int, sys.stdin.readline().split()))
cnt = 0

back_tracking(0,0)
print(cnt)