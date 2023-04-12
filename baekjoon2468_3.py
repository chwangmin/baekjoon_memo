import sys

sys.setrecursionlimit(10**8)

num = int(sys.stdin.readline())

water_board = [list(map(int,sys.stdin.readline().split()))for _ in range(num)]

count = 0

def dfs(x, y, h):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0<=nx<num) and (0<=ny<num) and not sink_board[nx][ny] and water_board[nx][ny] > h:
            sink_board[nx][ny] = True
            dfs(nx,ny,h)

check = 1

for k in range(max(map(max,water_board))):
    count = 0
    sink_board = [[False] * num for _ in range(num)]
    for i in range(num):
        for j in range(num):
            if not sink_board[i][j] and water_board[i][j] > k:
                count+=1
                sink_board[i][j] = True
                dfs(i,j,k)      
    check = max(check, count)

print(check)