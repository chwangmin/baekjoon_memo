import sys

input = sys.stdin.readline
import sys
import heapq

input = sys.stdin.readline

def bfs(x,y,cnt):
    heap = []
    heapq.heappush(heap,(cnt, x,y))
    
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    while heap:
        cnt, x, y = heapq.heappop(heap)
        if x == size-1 and y == size-1:
            print(cnt)
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= size or ny >= size or visited[nx][ny]:
                continue
            visited[nx][ny] = 1
            if board[nx][ny]:
                heapq.heappush(heap,(cnt,nx,ny))
            else:
                heapq.heappush(heap,(cnt+1,nx,ny))


size = int(input())

board = []

visited = [[0] * size for _ in range(size)]

for i in range(size):
    board.append(list(map(int,input().rstrip())))

bfs(0,0,0)