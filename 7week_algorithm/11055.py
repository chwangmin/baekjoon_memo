import sys

input = sys.stdin.readline

num = int(input())

num_list = list(map(int,input().split()))

dp = [1] * num

for i in range(num):
    tmp = num_list[i]
    for j in range(i):
        if num_list[j] < tmp and dp[i] <= dp[j]:
            dp[i] = dp[j] + 1

max_tmp = max(dp)

max_index = dp.index(max_tmp)

answer = [num_list[max_index]]

max_index_2 = max_tmp - 1

for i in range(max_index, -1, -1):
    if num_list[i] < num_list[max_index] and dp[i] == max_index_2:
        answer.append(num_list[i])
        max_tmp = i
        max_index_2 -= 1

answer.sort()

print(max(dp))
print(*answer)