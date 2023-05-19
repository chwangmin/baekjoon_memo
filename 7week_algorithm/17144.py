import sys

#sys.stdin = open('test.txt','r')

input = sys.stdin.readline

row, column, time = map(int,input().split())

mise_map = [list(map(int,input().split())) for _ in range(row)]

air_clean_p = 0

for i in range(row):
    if mise_map[i][0] == -1:
        air_clean_p = i
        break 

air_clean_b = air_clean_p + 1

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for t in range(time):
    tmp_map = [[0]*(column) for _ in range(row)]
    for i in range(row):
        for j in range(column):
            if mise_map[i][j] > 0:
                cnt = 0
                for k in range(4):
                    nx = i+dx[k]
                    ny = j+dy[k]
                    if 0 <= nx < row and 0 <= ny < column and mise_map[nx][ny] != -1 :
                        tmp_map[nx][ny] += mise_map[i][j] // 5
                        cnt += 1
                mise_map[i][j] -= (mise_map[i][j] // 5) * cnt
    for i in range(row):
        for j in range(column):
            if mise_map[i][j] == -1:
                continue
            mise_map[i][j] += tmp_map[i][j]
    for i in range(air_clean_p-1, 0, -1):
        mise_map[i][0] = mise_map[i-1][0]
    for i in range(column-1):
        mise_map[0][i] = mise_map[0][i+1]
    for i in range(air_clean_p):
        mise_map[i][column-1] = mise_map[i+1][column-1]
    for i in range(column-1,0,-1):
        if mise_map[air_clean_p][i-1] == -1:
            mise_map[air_clean_p][i] = 0
            continue
        mise_map[air_clean_p][i] = mise_map[air_clean_p][i-1]
    # 아래쪽 공기 청정기
    # 위로 이동 성공
    for i in range(air_clean_b+1, row-1, 1):
        mise_map[i][0] = mise_map[i+1][0]
    # 오른쪽으로 이동
    for i in range(column-1):
        mise_map[row-1][i] = mise_map[row-1][i+1]
    for i in range(row-1,air_clean_b,-1):
        mise_map[i][column-1] = mise_map[i-1][column-1]
    for i in range(column-1,0,-1):
        if mise_map[air_clean_b][i-1] == -1:
            mise_map[air_clean_b][i] = 0
            continue
        mise_map[air_clean_b][i] = mise_map[air_clean_b][i-1]

answer = 0
for i in range(row):
    for j in range(column):
        answer += mise_map[i][j]

print(answer+2)