import sys
from collections import deque

r, c = map(int,input().split())

arr = []
q = deque()

for _ in range(r):
    arr.append(list(sys.stdin.readline().rstrip()))


waterMap = [[-1] * c for _ in range(r)]
beaverMap = [[-1] * c for _ in range(r)]
start = []
end = []

for i in range(r):
    for j in range(c):
        if arr[i][j] == 'D':
            end = [i, j]
        elif arr[i][j] == 'S':
            start = [i, j]
            beaverMap[i][j] = 0
            arr[i][j] = '.'
        elif arr[i][j] == '*':
            q.append([i,j])
            waterMap[i][j] = 0

dir = [[-1,0], [1,0], [0,-1], [0,1]]

while q:
    x, y = q.popleft()
    for i in range(4):
        dx = x + dir[i][0]
        dy = y + dir[i][1]
        if 0 <= dx < r and 0 <= dy < c and arr[dx][dy] == '.' and waterMap[dx][dy] == -1:
            if beaverMap[x][y] + 1 < waterMap[dx][dy] or waterMap[dx][dy] == -1:
                beaverMap[dx][dy] = beaverMap[x][y] + 1
                q.append([dx,dy])

if beaverMap[end[0]][end[1]] == -1:
    print('KAKTUS')
else:
    print(beaverMap[end[0]][end[1]])