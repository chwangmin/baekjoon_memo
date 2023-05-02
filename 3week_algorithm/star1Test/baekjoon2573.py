import sys

input = sys.stdin.readline

row, column = map(int,input().split())

graph = [[[] for _ in range(column)] for _ in range(row)]

matrix = []

for _ in range(row):
    matrix.append(list(map(int,input().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for x in range(row):
    for y in range(column):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < column:
                if matrix[nx][ny] and matrix[x][y]:
                    graph[x][y].append((nx,ny,matrix[nx][ny]))

print(graph)
