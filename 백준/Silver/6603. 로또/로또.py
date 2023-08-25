import sys

input = sys.stdin.readline

def dfs(depth, idx):
    if depth == 6:
        print(*stackAnswer)
        return
    
    for i in range(idx,k):
        stackAnswer.append(S[i])
        dfs(depth + 1, i + 1)
        stackAnswer.pop()

while(1):
    listNum = list(map(int,input().split()))
    k = listNum[0]
    S = listNum[1:]
    stackAnswer = []
    dfs(0,0)

    if k == 0:
        break

    print()