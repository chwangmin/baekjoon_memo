import sys

input = sys.stdin.readline

N, K = map(int,input().split())

answer = 1

dp = [[1] * N for _ in range(K)]

if K > 1:
    for i in range(N):
        dp[1][i] = i+2

for i in range(2,K):
    for j in range(N):
        if j == 0:
            dp[i][j] = i+1
            continue
        dp[i][j] = dp[i-1][j] + dp[i][j-1] % 1_000_000_000
print(dp[-1][-1] % 1_000_000_000)