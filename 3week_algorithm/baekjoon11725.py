import sys

input = sys.stdin.readline

def dfs(node):
    visited[node] = 1
    for child in graph[node]:
        if not visited[child]:
            answer[child] = node
            dfs(child)

node_num = int(input())

graph = [[]*(node_num+1) for _ in range(node_num+1)]
visited = [0] * (node_num+1)
answer = [0] * (node_num+1)

while True:
    try:
        a, b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    except:
        break

dfs(1)

print(*answer[2:], sep='\n')