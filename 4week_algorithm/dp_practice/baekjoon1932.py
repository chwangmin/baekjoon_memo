import sys

input = sys.stdin.readline

num = int(input())

dp = []

for i in range(num):
    dp.append(list(map(int,input().split())))

for i in range(1, num):
    for j in range(i+1):
        if j == 0:
            dp[i][j] += dp[i-1][j]
        elif j == i:
            dp[i][j] += dp[i-1][-1]
        else:
            dp[i][j] += max(dp[i-1][j-1],dp[i-1][j])

print(max(dp[num-1]))
