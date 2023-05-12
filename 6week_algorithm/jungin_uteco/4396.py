import sys

input = sys.stdin.readline

num = int(input())

mine_map = []

check_map = []

answer_map=[]

tmp_map = [[0]*(num+2) for _ in range(num+2)]

for i in range(num):
    mine_map.append(list(input().rstrip()))

for i in range(num):
    check_map.append(list(input().rstrip()))

arrow = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

for i in range(num):
    for j in range(num):
        if mine_map[i][j] == '*':
            for k in range(8):
                tmp_map[(i+1)-arrow[k][0]][(j+1)-arrow[k][1]] += 1

visited = 0

for i in range(num):
    for j in range(num):
        if check_map[i][j] == '.':
            tmp_map[i+1][j+1] = '.'

for i in range(num):
    for j in range(num):
        if not visited and check_map[i][j] == 'x' and mine_map[i][j] == '*':
            visited = 1
            for x in range(num):
                for y in range(num):
                    if mine_map[x][y] == '*':
                        tmp_map[x+1][y+1] = '*'
            break
    if visited:
        break

for i in range(1,num+1):
    for j in range(1,num+1):
        print(tmp_map[i][j], end ='')
    print()
