import sys

input = sys.stdin.readline

def find_parrent(parrent, x):
    if parrent[x] != x:
        parrent[x] = find_parrent(parrent,parrent[x])
    return parrent[x]

def union_parrent(parrent,a,b):
    a = find_parrent(parrent,a)
    b = find_parrent(parrent,b)
    if a < b:
        parrent[b] = a
    else:
        parrent[a] = b
    

verticles, edge = map(int,input().split())

parrent = [0] * (verticles+1)

list_edges = []

for i in range(1, verticles+1):
    parrent[i] = i
for _ in range(edge):
    list_edges.append(list(map(int,input().split())))

list_edges.sort(key=lambda x: (x[2]))

answer = 0

for edge2 in list_edges:
    if find_parrent(parrent, edge2[0]) == find_parrent(parrent, edge2[1]):
        continue
    else:
        union_parrent(parrent, edge2[0], edge2[1])
        answer += edge2[2]

print(answer)

