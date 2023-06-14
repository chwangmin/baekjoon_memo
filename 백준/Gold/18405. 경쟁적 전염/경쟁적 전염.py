import sys
from collections import deque

#sys.stdin = open("test.txt",'r')

input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    q = deque(virus)
    count = 0
    while q:
        if count == time_cnt:
            break
        for _ in range(len(q)):
            virus_num, x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N and examiner_map[nx][ny] == 0:
                    examiner_map[nx][ny] = virus_num
                    q.append([virus_num,nx,ny])
        count+=1
    
    

N, K = map(int,input().split())

examiner_map = []

virus = []

for i in range(N):
    examiner_map.append(list(map(int,input().split())))
    for j in range(N):
        if examiner_map[i][j]:
            virus.append([examiner_map[i][j],i,j])

virus.sort()

time_cnt, row, column = map(int,input().split())


bfs()

print(examiner_map[row-1][column-1])
