import sys

input = sys.stdin.readline

def bfs(x,y,arrow_check):
    cnt = 0
    stack = []
    stack.append((x,y,arrow_check))
    while stack:
        x,y,arrow_check = stack.pop()
        if clean_map[x][y] == 0:
            clean_map[x][y] = -1
            cnt +=1
        check_nothing_dirty = 1
        for i in range(3,-1,-1):
            arrow_current = arrow_change(arrow_check + i)
            if clean_map[x+arrow_current[0]][y+arrow_current[1]] == 0:
                check_nothing_dirty = 0
                nx = x+arrow_current[0]
                ny = y+arrow_current[1]
                stack.append((nx,ny,arrow_check + i))
                break
        if check_nothing_dirty:
            arrow_current = arrow_change(arrow_check+2)
            if clean_map[x+arrow_current[0]][y+arrow_current[1]] == 1:
                return cnt
            else:
                stack.append((x+arrow_current[0],y+arrow_current[1],arrow_check))
                continue
    return cnt


def arrow_change(arrow_check):
    arrow_check %= 4
    arrow_list = [(-1,0),(0,1),(1,0),(0,-1)]
    arrow_current = arrow_list[arrow_check]
    return arrow_current

row, column = map(int,input().split())

start_x, start_y, arrow_check = map(int,input().split())

clean_map = [list(map(int,input().split())) for _ in range(row)]

print(bfs(start_x, start_y, arrow_check))