import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

def dfs(x, cnt):
    visited[x] = 1
    for i in list_node[x]:
        if list_node_check[i] == 1:
            cnt += 1
        elif not visited[i] and list_node_check[i] == 0:
            cnt = dfs(i,cnt)
    return cnt

num_node = int(input())

list_node_check = [0] + list(map(int,input().rstrip()))

list_node = [[] for _ in range(num_node + 1)]

visited = [0] * (num_node + 1)

answer = 0

for _ in range(num_node-1):
    x, y = map(int,input().split())
    list_node[x].append(y)
    list_node[y].append(x)
    if list_node_check[x] == 1 and list_node_check[y] == 1:
        answer +=2

for i in range(1, num_node+1):
    if not visited[i] and list_node_check[i] == 0:
        tmp = dfs(i, 0)
        answer += tmp*(tmp-1)

print(answer)