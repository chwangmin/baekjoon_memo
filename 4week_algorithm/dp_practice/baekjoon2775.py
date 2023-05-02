import sys

input = sys.stdin.readline

num = int(input())

for _ in range(num):
    floor = int(input())
    ho = int(input())

    dp = [[0] * ho for _ in range(floor + 1)]

    for i in range(ho):
        dp[0][i] = i+1
    for i in range(1, floor + 1):
        for j in range(ho):
            if j == 0:
                dp[i][j] = 1
                continue
            dp[i][j] = dp[i][j-1] + dp[i-1][j]
    print(dp[floor][ho-1])

