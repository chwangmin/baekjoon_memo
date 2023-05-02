import sys

input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(x,y):
    x = find_parent(x)
    y = find_parent(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

vertexs, edges = map(int,input().split())

list_tmp = []

for i in range(edges):
    a, b, c = map(int,input().split())

    list_tmp.append((a,b,c))

list_tmp.sort(key=lambda x: (x[2]))

parent = [0] * (vertexs + 1)

for i in range(1, vertexs+1):
    parent[i] = i

count = 0

for i in range(edges):
    x = list_tmp[i][0]
    y = list_tmp[i][1]
    weight = list_tmp[i][2]

    if find_parent(x) == find_parent(y):
        continue
    else:
        union_parent(x,y)
        count += weight

print(count)