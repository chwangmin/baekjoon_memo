import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def dfs(x):
    visited[x] = 1
    for i in graph[x]:
        if not visited[i]:
            parent[i] = x
            dfs(i)


num = int(input())

visited = [0] * (num+1)

graph = [[] for _ in range(num + 1)]

parent = [0] * (num + 1)

# 트리의 루트는 1
while True:
    try:
        a, b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    except:
        break

dfs(1)

for i in range(2, num+1):
    print(parent[i])
