import sys

input = sys.stdin.readline

num_matrix = int(input())

list_matrix = []

dp = [[0] * (num_matrix) for _ in range(num_matrix)]

for _ in range(num_matrix):
    list_matrix.append(list(map(int,input().split())))

for size in range(1, num_matrix):
    for start in range(num_matrix - size):
        end = start + size

        result = float("inf")
        for cut in range(start,end):
            result = min(result, dp[start][cut] + dp[cut+1][end] + list_matrix[start][0] * list_matrix[cut][1] * list_matrix[end][1])
        dp[start][end] = result
        
print(dp[0][-1])