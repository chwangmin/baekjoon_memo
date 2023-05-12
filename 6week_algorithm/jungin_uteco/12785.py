import sys

input = sys.stdin.readline

map_x, map_y = map(int,input().split())

toast_x, toast_y = map(int,input().split())

dp = [[1] * map_y for _ in range(map_x)]

for i in range(1, map_x):
    for j in range(1, map_y):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]

go_toast_int = dp[toast_x-1][toast_y-1]

if toast_x == map_x and toast_y == toast_y:
    print(go_toast_int % 1000007)
    exit()

go_toast_map_int = dp[map_x-toast_x][map_y-toast_y]

print((go_toast_int*go_toast_map_int) % 1000007)