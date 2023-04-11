import sys

def dfs(start, now, value, cnt):
    global ans
    if cnt == num:
        if a[now][start]:
            value += a[now][start]
            if ans > value:
                ans = value

    if value > ans:
        return
    
    for i in range(num):
        if not visited[i] and a[now][i]:
            visited[i] = 1
            dfs(start, i, value + a[now][i], cnt+1)
            visited[i] = 0

        
num = int(sys.stdin.readline())
ans = sys.maxsize
visited = [0] * num
a = [list(map(int,sys.stdin.readline().split()))for _ in range(num)] 
for i in range(num):
    visited[i] = 1
    dfs(i,i,0,1)
    visited[i] = 0

print(ans)