import sys

input = sys.stdin.readline

def parent_find(tmp):
    if list_parent[tmp] != tmp:
        list_parent[tmp] = parent_find(list_parent[tmp])
    return list_parent[tmp]

def union(tmp1, tmp2):
    tmp1 = parent_find(tmp1)
    tmp2 = parent_find(tmp2)
    if tmp1 < tmp2:
        list_parent[tmp2] = list_parent[tmp1]
    else:
        list_parent[tmp1] = list_parent[tmp2]
        
n, m = map(int,input().split())

list_parent = list(range(n+1))

for i in range(m):
    tmp1, tmp2 = map(int,input().split())
    union(tmp1,tmp2)

input()

edges = []

for i in range(1,n):
    ins = list(map(int,input().split()))
    for j in range(i+1,n):
        edges.append((ins[j],i+1,j+1))
edges.sort()

x = 0
k = 0
res = []

for edge in edges:
    if parent_find(edge[1])!=parent_find(edge[2]):
        union(edge[1],edge[2])
        x += edge[0]
        k +=1
        res.append((edge[2],edge[1]))

print(x,k)
for i in res:
    print(i[0],i[1])