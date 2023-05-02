import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    stack = deque()
    stack.append((x,y))
    while stack:
        x, y = stack.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<row and 0<=ny<column:
                if matrix[nx][ny] == 1:
                    matrix[nx][ny] = matrix[x][y] + 1
                    stack.append((nx,ny))


row, column = map(int,input().split())

matrix = []


for i in range(row):
    matrix.append(list(map(int,input().rstrip())))

bfs(0,0)

print(matrix[row-1][column-1])