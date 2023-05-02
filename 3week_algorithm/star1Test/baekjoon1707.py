import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def dfs(x, color):
    visited[x] = 1
    color_tmp[x] = color
    for i in graph[x]:
        if color_tmp[x] == color_tmp[i]:
            global flag
            flag = 1
            return
        if color_tmp[i] == -1 and not visited[i]:
            color = (color_tmp[x] + 1) % 2
            dfs(i, color)

num_case = int(input())

for _ in range(num_case):
    vertexs, edges = map(int,input().split())

    flag = 0

    graph = [[] for _ in range(vertexs+1)]
    color_tmp = [-1] * (vertexs + 1)
    visited = [0] * (vertexs + 1)

    for _ in range(edges):
        x, y = map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)
    
    for i in range(1, vertexs+1):
        if not visited[i]:
            dfs(i, 1)

    if flag:
        print("NO")
    else:
        print("YES")