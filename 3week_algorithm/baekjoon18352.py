import sys
from collections import deque

input = sys.stdin.readline

def bfs(a):
    queue = deque()
    visited[a] = 1
    queue.append(a)
    while queue:
        a = queue.popleft()
        for i in matrix[a]:
            if visited[i] == 0:
                visited[i] = 1
                distance[i] = distance[a] + 1
                queue.append(i)


N, M, K, X = map(int,input().split())

matrix = [[] * (N+1) for _ in range(N+1)]

visited = [0] * (N+1)
distance = [0] * (N+1)

for i in range(M):
    x, y = map(int,input().split())

    matrix[x].append(y)

bfs(X)

if distance.count(K) > 0:
    for i in range(1,N+1):
        if distance[i] == K:
            print(i)
else:
    print(-1)