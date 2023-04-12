import sys

num = int(sys.stdin.readline())

a = [list(map(int,sys.stdin.readline().split())) for _ in range(num)]

val = sys.maxsize

visited = [False] * num

def dfs(start, now, value, cnt):
    global val
    if cnt == num-1:
        if a[now][start]:
            value += a[now][start]
            if val > value:
                val = value
    if val < value:
        return
    for i in range(num):
        if a[now][i] and not visited[i]:
            visited[i] = True
            dfs(start,i,value+a[now][i],cnt+1)
            visited[i] = False 

for i in range(num):
    visited[i] = True
    dfs(i,i,0,0)
    visited[i] = False

print(val)