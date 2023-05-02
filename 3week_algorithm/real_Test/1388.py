import sys

input = sys.stdin.readline

def check_garo(x, y):
    visited[x][y] = 1
    ny = y + 1
    if ny >= column:
        return
    if map_check[x][ny] == '-':
        check_garo(x,ny)

def check_sero(x, y):
    visited[x][y] = 1
    nx = x + 1
    if nx >= row:
        return
    if map_check[nx][y] == '|':
        check_sero(nx,y)
    return

row, column = map(int,input().split())

map_check = []

visited = [[0] * column for _ in range(row)]

for i in range(row):
    map_check.append(list(map(str,input().rstrip())))

count = 0

for i in range(row):
    for j in range(column):
        if not visited[i][j]:
            if map_check[i][j] == '-':
                check_garo(i,j)
                count += 1
            if map_check[i][j] == '|':
                check_sero(i,j)
                count += 1

print(count)