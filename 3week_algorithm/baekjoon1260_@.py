import sys
from collections import deque

input = sys.stdin.readline

def dfs(start):
    visited[start] = 1
    print(start, end=' ')

    for i in range(1, verticles+1):
        if not visited[i] and s[start][i]:
            dfs(i)

def bfs(start):
    q = deque([start])
    visited = 0
    while q:
        start = q.popleft()
        print(start, end=" ")
        for i in range(1, verticles + 1):
            if visited[i] and s[start][i]:
                q.append(i)
                visited[i] = 0

verticles, edges, start = map(int,input().split())

s = [[0] * (verticles + 1) for _ in range(verticles+1)]

visited = [0] * (verticles + 1)

for _ in range(edges):
    x1, x2 = map(int,input().split())
    
    s[x1][x2] = 1
    s[x2][x1] = 1

dfs(start)
print()
bfs(start)