# 시간 초과 bfs로 다시 풀어봐야 함.

import sys
from collections import deque

input = sys.stdin.readline

def bfs(x,y):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    queue = deque()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < si_size and 0 <= ny < si_size:
            queue.append((nx,ny))
    
    while queue:
        cx, cy = queue.popleft()
        if si_matrix[cx][cy] == si_matrix[x][y]:
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                queue.append((nx,ny))

si_size, birus_num = map(int,input().split())

si_matrix = []

for i in range(si_size):
    si_matrix.append(list(map(int,input().split())))

time, answer_X, answer_Y = map(int,input().split())

for t in range(1, time+1): # time+1
    check_in_time = [[0]*si_size for _ in range(si_size)]
    for i in range(si_size):
        for j in range(si_size):
            if si_matrix[i][j]:
                dfs(i,j)

print(si_matrix)

print(si_matrix[answer_X-1][answer_Y-1])

# input = sys.stdin.readline

# def dfs(x,y,num):
#     dx = [1,-1,0,0]
#     dy = [0,0,1,-1]
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < si_size and 0 <= ny < si_size and not visited[nx][ny] and not visited[x][y]:
#             if si_matrix[nx][ny] == 0 and si_matrix[x][y] == num:
#                 si_matrix[nx][ny] = num
#                 visited[nx][ny] = 1
#                 dfs(nx,ny,num)

# si_size, birus_num = map(int,input().split())

# si_matrix = []

# for i in range(si_size):
#     si_matrix.append(list(map(int,input().split())))

# time, answer_X, answer_Y = map(int,input().split())

# for t in range(1, time+1):
#     visited = [[0]*si_size for _ in range(si_size)]
#     for num in range(1, birus_num+1):
#         for i in range(si_size):
#             for j in range(si_size):
#                 if si_matrix[i][j] == num:
#                     dfs(i,j,num)

# print(si_matrix[answer_X-1][answer_Y-1])