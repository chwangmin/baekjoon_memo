# Pass

import sys

input = sys.stdin.readline

def dfs(x,y,cnt):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    if 0 <= x < column and 0 <= y < row:
        if x == column-1 and y == row-1:
            cnt+=1
    return cnt


row, column = map(int,input().split())

map_list = [list(map(int,input().split())) for _ in range(row)]

dp = [[0] * column for _ in range(row)]

dp[0][0] = 1

dfs(0,0,0)