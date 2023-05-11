# 성공

import sys

input = sys.stdin.readline

num = int(input())

list_num = [list(map(int,input().split())) for _ in range(num)]

dp = [[0] * num for _ in range(num)]

dp[0][0] = 1

for i in range(num):
    for j in range(num):
        if i == num-1 and j == num-1:
            break
        if dp[i][j]:
            if i+list_num[i][j] < num:
                dp[i+list_num[i][j]][j] += dp[i][j]
            if j+list_num[i][j] < num:
                dp[i][j+list_num[i][j]] += dp[i][j]

print(dp[num-1][num-1])

# # dfs 시간 초과 실패
# import sys

# input = sys.stdin.readline

# def dfs(x,y,cnt):
#     if 0 <= x < num and 0 <= y < num:
#         if x == num-1 and y == num-1:
#             cnt+=1
#         else:
#             cnt = dfs(x+list_num[x][y], y,cnt)
#             cnt = dfs(x,y+list_num[x][y],cnt)
#     return cnt
    


# num = int(input())

# list_num = [list(map(int,input().split())) for _ in range(num)]

# print(dfs(0, 0, 0))