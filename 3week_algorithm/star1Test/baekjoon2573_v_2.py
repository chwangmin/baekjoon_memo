import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def spread(x,y):
    if visited[x][y]:
        return
    visited[x][y] = 1
    minus_cnt = 0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 > nx or nx >= row or 0 > ny or ny >= column or visited[nx][ny]:
            continue
        if board[nx][ny] <= 0:
            board_tmp[x][y] -= 1
        if board[nx][ny] > 0:
            spread(nx,ny)

row, column = map(int,input().split())

board = []

max_check = -1

for _ in range(row):
    list_check = list(map(int,input().split()))
    board.append(list_check)

board_tmp = board

answer = 0

for h in range(sys.maxsize):
    cnt = 0
    visited = [[0]*column for _ in range(row)]
    for x in range(row):
        for y in range(column):
            if board[x][y] > 0 and not visited[x][y]:
                spread(x,y)
                cnt += 1
    board = board_tmp
    if cnt >= 2:
        print(answer)
        break
    elif cnt == 0:
        print(0)
        break
    else:
        answer += 1