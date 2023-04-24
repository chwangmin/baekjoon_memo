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

computers = int(input())
edges = int(input())

parrent = [0] * (computers + 1)

for i in range(1, computers+1):
    parrent[i] = i

for _ in range(edges):
    x1, x2 = map(int,input().split())

    union_parrent(x1, x2)

cnt = -1

for i in range(1,computers+1):
    parrent[i] = find_parrent(parrent[i])

for i in parrent:
    if i == 1:
        cnt += 1

print(cnt)
