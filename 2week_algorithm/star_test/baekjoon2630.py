import sys

input = sys.stdin.readline

N = int(input())

board = [list(map(int,input().split())) for _ in range(N)]

check_white = 0
check_blue = 0

def check_board(x_start, y_start, x_N, y_N):
    global check_white, check_blue
    check = board[x_start][y_start]
    nx = x_N - x_start
    ny = y_N - y_start
    for i in range(x_start,x_N):
        for j in range(y_start,y_N):
            if board[i][j] != check:
                check_board(x_start,y_start,x_N-nx//2,y_N-ny//2)
                check_board(x_start + nx//2, y_start, x_N, y_N-ny//2)
                check_board(x_start, y_start + ny//2,x_N-nx//2,y_N)
                check_board(x_start + nx//2, y_start + ny//2, x_N, y_N)
                return
    if check == 0:
        check_white += 1
    else:
        check_blue += 1 

check_board(0,0,N,N)

print(check_white)
print(check_blue)