import sys

input = sys.stdin.readline

n, m = map(int,input().split())

num_list = [list(map(int,input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i > 0 and j > 0:
            dp[i][j] = dp[i-1][j] + dp[i][j-1] + num_list[i][j] - dp[i-1][j-1]
            continue
        elif i == 0:
            if j == 0:
                dp[i][j] = num_list[i][j]
                continue
            dp[i][j] += dp[i][j-1] + num_list[i][j]
        else:
            dp[i][j] = dp[i-1][j] + num_list[i][j]

print(dp)
for _ in range(m):
    x1, y1, x2, y2 = map(int,input().split())
    x1 -= 1
    x2 -= 1
    y1 -= 1
    y2 -= 1
    if x1 == 0 and y1 == 0:
        print(dp[x2][y2])
    elif x1 == 0:
        print(dp[x2][y2] - dp[x2][y1-1])
    elif y1 == 0:
        print(dp[x2][y2] - dp[x1-1][y2])
    else:
        print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])