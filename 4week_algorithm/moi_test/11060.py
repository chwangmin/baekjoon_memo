import sys

input = sys.stdin.readline

num = int(input())

list_num = [0] + list(map(int,input().split()))

if num == 1:
    print(0)
    exit()

dp = [[float("INF")] * (max(list_num)+1) for _ in range(num+1)]

dp[1][1] = 0

cnt = 0
for i in range(1,num):
    if list_num[i] == 0 or min(dp[i]) == float("INF"):
         continue
    for j in range(1,list_num[i] + 1):
        if i+j > num:
            continue
        dp[i+j][j] = min(dp[i+j][j], min(dp[i])) + 1
        if dp[i+j][j] < 100000 and i+j == num:
            print(min(dp[-1]))
            exit()

print(-1)