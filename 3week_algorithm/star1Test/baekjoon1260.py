import sys

from collections import deque

input = sys.stdin.readline

def dfs(x):
    print(x, end =' ')
    visited[x] = 1
    for i in graph[x]:
        if not visited[i]:
            dfs(i)

def bfs(x):
    visited[x] = 0
    queue = deque()
    queue.append(x)
    while queue:
        x = queue.popleft()
        print(x, end =' ')
        for i in graph[x]:
            if visited[i]:
                visited[i] = 0
                queue.append(i)

vertexs, edges, start_vertex = map(int,input().split())

visited = [0] * (vertexs + 1)

graph = [[] for _ in range(vertexs+1)]

for _ in range(edges):
    a, b = map(int,input().split())

    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

dfs(start_vertex)
print()
bfs(start_vertex)