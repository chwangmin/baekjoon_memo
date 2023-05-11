import sys

input = sys.stdin.readline

num_rock, num_small_rock = map(int,input().split())

list_small_rock = [int(input()) for _ in range(num_small_rock)]

# list_small_rock = set()

# for _ in range(num_small_rock):
#     list_small_rock.add(int(input()))

dp = [[float('inf')] * (int((2 * num_rock) ** 0.5)+2) for _ in range(num_rock + 1)]

dp[1][0] = 0

for i in range(2, num_rock + 1):
    if i in list_small_rock:
        continue
    for j in range(1, int((2 * i) ** 0.5) + 1):
        dp[i][j] = min(dp[i-j][j-1], dp[i-j][j], dp[i-j][j+1]) + 1

if min(dp[num_rock]) == float('inf'):
    print(-1)
else:
    print(min(dp[num_rock]))