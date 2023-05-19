import sys

sys.setrecursionlimit(10**6)

#sys.stdin = open('test.txt','r')

input = sys.stdin.readline

def dfs(i,j,cnt):
    visited[i][j] = 1
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for k in range(4):
        nx = i+dx[k]
        ny = j+dy[k]
        if 0<=nx<column and 0<=ny<row and not visited[nx][ny] and tong_map[nx][ny]:
            cnt = dfs(nx,ny,cnt+1)
    return cnt


column, row, num = map(int,input().split())

tong_map = [[0]*row for i in range(column)]

visited = [[0]*row for i in range(column)]

for i in range(num):
    x, y = map(int,input().split())

    tong_map[x-1][y-1] = 1

answer = 0

for i in range(column):
    for j in range(row):
        if not visited[i][j] and tong_map[i][j]:
            cnt = dfs(i,j,0)
            if cnt > answer:
                answer = cnt

print(answer+1)