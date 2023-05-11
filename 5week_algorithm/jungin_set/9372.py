import sys

input = sys.stdin.readline

def dfs(x,cnt):
    visited[x] = 1
    for i in graph[x]:
        if not visited[i]:
            cnt = dfs(i,cnt+1)
    return cnt

T = int(input())
for i in range(T):
    nation_num, airplane_num = map(int,input().split())

    graph=[[]for _ in range(nation_num + 1)]

    visited = [1] + [0] * (nation_num)

    for i in range(airplane_num):
        x, y = map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)

    print(dfs(1,0))
