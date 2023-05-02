import sys

input = sys.stdin.readline

def check_gatungi(x,y,dan_num):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    visited[x][y] = 1
    answer[dan_num] += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < map_size and 0 <= ny < map_size and not visited[nx][ny]:
            if map_graph[nx][ny] == 1:
                check_gatungi(nx,ny,dan_num)


map_size = int(input())

map_graph = []

answer = [0] * 626


for i in range(map_size):
    tmp = list(map(int,input().rstrip()))
    map_graph.append(tmp)

dan_num = 1
visited = [[0] * map_size for _ in range(map_size)]
for i in range(map_size):
    for j in range(map_size):
        if not visited[i][j] and map_graph[i][j] == 1:
            check_gatungi(i,j,dan_num)
            dan_num += 1

answer.sort(reverse=True)

print(dan_num-1)
for i in range(0, dan_num-1):
    print(answer[dan_num-i-2])