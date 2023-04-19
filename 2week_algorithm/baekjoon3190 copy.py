from collections import deque

N = int(input())

apple_num = int(input())
apple_board = [[0] * N for _ in range(N)]

for i in range(apple_num):
    apple_x, apple_y = map(int,input().split())
    apple_board[apple_x][apple_y] = 1

snake_turn_num = int(input())
snake_turn_list = []

for i in range(snake_turn_num):
    count, turn = map(str,input().split())
    count = int(count)
    snake_turn_list.append((count,turn))

snake_turn_list.append((10001,''))

snake = deque()
snake.append((0,0))

start = 1
breaker = False
cnt = 0

arrow_list = [(1,0),(0,1),(-1,0),(0,-1)]
arrow_check = 0

def snake_turn(arrow):
    global arrow_check
    if arrow == "D":
        if arrow_check != 3:
            arrow_check += 1
        else:
            arrow_check = 0
    else:
        if arrow_check != 0:
            arrow_check -= 1
        else:
            arrow_check = 3
        
x , y = 0, 0

for i in range(len(snake_turn_list)):
    start = cnt + 1
    for _ in range(start, snake_turn_list[i][0] + 1):
        nx = x + arrow_list[arrow_check][0]
        ny = y + arrow_list[arrow_check][1]
        if nx < 0 or ny < 0 or nx >= N or ny >= N or (nx,ny) in snake:
            cnt += 1
            breaker = True
            break
        if apple_board[nx][ny]:
            apple_board[nx][ny] = 0
            snake.append((nx,ny))
            x, y = nx, ny
        else:
            snake.append((nx,ny))
            snake.popleft()
            x, y = nx, ny
        cnt +=1
    if breaker:
        break
    snake_turn(snake_turn_list[i][1])

print(cnt)