import sys
from collections import deque

input = sys.stdin.readline

board_size = int(input())

apple_num = int(input())

apple_board = [[0] * board_size for _ in range(board_size)]

for i in range(apple_num):
    x, y = map(int,input().split())
    x, y = x - 1, y - 1
    apple_board[y][x] = 1

snake_turn_num = int(input())
snake_turn = []

for i in range(snake_turn_num):
    count, arrow = map(str,input().split())
    snake_turn.append((int(count),arrow))

snake_turn.append((10001,''))

list_arrow = [(1,0),(0,1),(-1,0),(0, -1)]
check_arrow_num = 0

def change_arrow(arrow):
    global check_arrow_num
    if arrow == 'D':
        if check_arrow_num == 3:
            check_arrow_num = 0
        else:
            check_arrow_num += 1
    else:
        if check_arrow_num == 0:
            check_arrow_num = 3
        else:
            check_arrow_num -= 1

cnt = 0

x, y = 0, 0
snake = deque()
snake.append((x,y))
breaker = False
start = 1

for i in range(len(snake_turn)):
    start = cnt + 1
    for _ in range(start, snake_turn[i][0] + 1):
        nx = x + list_arrow[check_arrow_num][0]
        ny = y + list_arrow[check_arrow_num][1]
        if nx < 0 or ny < 0 or nx >= board_size or ny >= board_size or (nx,ny) in snake:
            cnt += 1
            breaker = True
            break
        if apple_board[nx][ny]:
            x, y = nx, ny
            snake.append((nx,ny))
            apple_board[nx][ny] = 0
        else:
            x, y = nx, ny
            snake.append((nx,ny))
            snake.popleft()
        cnt += 1
    if breaker:
        break
    change_arrow(snake_turn[i][1])

print(cnt)
