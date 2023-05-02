import sys

input = sys.stdin.readline

num = int(input())

dp = [0] * (num)

dp[1] = 1
dp[2] = 2

for i in range(3, num):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[num-1])
print(num-2)