import sys

sys.setrecursionlimit(10**8)

num = int(sys.stdin.readline())
water_board = [list(map(int,sys.stdin.readline().split()))for _ in range(num)]

check = 1

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def water_DFS(x,y,k):
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if (0<=nx<num) and (0<=ny<num) and water_board[nx][ny] > k and not sink_board[nx][ny]:
            sink_board[nx][ny] = True
            water_DFS(nx,ny,k)

for k in range(max(map(max,water_board))):
    count = 0
    sink_board = [[False] * num for _ in range(num)]
    for i in range(num):
        for j in range(num):
            if water_board[i][j] > k and not sink_board[i][j]:
                count+=1
                sink_board[i][j] = True
                water_DFS(i,j,k)
    check = max(check, count)

print(check)