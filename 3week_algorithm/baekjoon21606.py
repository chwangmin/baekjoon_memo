import sys

input = sys.stdin.readline

def dfs(x):
    global cnt
    for i in abjecent[x]:
        if list_inout[i-1] == 0:
            dfs(i)
        else:
            cnt +=1

cnt = 0

num = int(input())

list_inout = input()

abjecent = [[] * (num+1) for _ in range(num+1)]

while True:
    try:
        x, y = map(int,input().split())
        abjecent[x].append(y)
        abjecent[y].append(x)
    except:
        break

for i in range(len(list_inout)):
    if list_inout[i] == 0:
        continue
    dfs(i)

print(cnt)