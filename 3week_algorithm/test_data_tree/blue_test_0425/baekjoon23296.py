import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def dfs(x):
    if not cleaned.count(0):
        print(len(answer))
        print(*answer)
        exit()
    cleaned[x] = 1
    for i in graph[x]:
        if find_parent(x) == find_parent(i):
            result = sys.maxsize
            for i in range(1, floor_num+1):
                if cleaned[i] == 0:
                    if result > abs(i-x):
                        result = abs(i-x)
                        tmp = i
            if result > 123456789:
                exit()
            else:
                answer.append(tmp)
                dfs(tmp)
        else:
            union_find(x,i)
            answer.append(i)
            dfs(i)


def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_find(x, y):
    if x < y:
        parent[y] = find_parent(x)
    else:
        parent[x] = find_parent(y)

floor_num = int(input())

graph = [[] for _ in range(floor_num+1)]

tmp_list = list(map(int,input().split()))

parent = [0] * (floor_num + 1)

cleaned = [1] + [0] * (floor_num)

answer = []

for i in range(1, floor_num+1):
    parent[i] = i

for i in range(1, floor_num+1):
    graph[i].append(tmp_list[i-1])

dfs(1)