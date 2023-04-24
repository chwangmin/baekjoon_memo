import sys

input = sys.stdin.readline

def find_parrent(x):
    if parrent[x] != x:
        parrent[x] = find_parrent(parrent[x])
    return parrent[x]

def union_parrent(x1, x2):
    a = find_parrent(x1)
    b = find_parrent(x2)
    if a < b:
        parrent[x2] = a
        parrent[b] = a 
    else:
        parrent[x1] = b
        parrent[a] = b
        

verticles, edges = map(int,input().split())

parrent = [0] * (verticles + 1)

for i in range(1, verticles + 1):
    parrent[i] = i

for i in range(edges):
    x1, x2 = map(int,input().split())
    union_parrent(x1,x2)

for i in range(1, verticles+1):
    parrent[i] = find_parrent(parrent[i])

print(len(set(parrent))-1)
