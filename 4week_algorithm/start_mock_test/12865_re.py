import sys

input = sys.stdin.readline

num_things, bag_size = map(int,input().split())

list_things = []

for _ in range(num_things):
    list_things.append(list(map(int,input().split())))

dp = [[0]*(bag_size + 1) for _ in range(num_things + 1)]

k = 1

for thing in list_things:
    for i in range(1, bag_size + 1):
        if thing[0] <= i:
            dp[k][i] = max(dp[k-1][i], thing[1] + dp[k-1][i-thing[0]])
        else:
            dp[k][i] = dp[k-1][i]
    print(dp[k])
    k+=1

print(dp[num_things][bag_size])