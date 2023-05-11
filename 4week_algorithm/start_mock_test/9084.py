import sys

input = sys.stdin.readline

num_Test = int(input())

for _ in range(num_Test):
    num_Coin = int(input())
    list_Coin = list(map(int,input().split()))
    make_Money = int(input())
    dp = [[0] * (make_Money + 1) for _ in range(num_Coin + 1)]
    k = 1
    for i in range(num_Coin+1):
        dp[i][0] = 1
    for coin in list_Coin:
        for i in range(1, make_Money + 1):
            if i >= coin:
                dp[k][i] = dp[k-1][i] + dp[k][i-coin]
            else:
                dp[k][i] = dp[k-1][i]
        k += 1
    print(dp[num_Coin][make_Money])