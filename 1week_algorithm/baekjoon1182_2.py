import sys

N,S=map(int, sys.stdin.readline().split())
sequence=list(map(int, sys.stdin.readline().split()))

def BFS(depth, number):
    global answer
    if depth == N:
        if S == number:
            answer+=1
        return
    BFS(depth+1,number)
    BFS(depth+1,number+sequence[depth])
answer = 0
BFS(0,0)
if S == 0: answer -=1
print(answer)