import sys

input = sys.stdin.readline

num = int(input())

wanted_score_list = []

for _ in range(num):
    wanted_score_list.append(int(input()))

wanted_score_list.sort()

answer = 0

for i in range(num):
    if wanted_score_list[i] != i+1:
        answer += abs(wanted_score_list[i]-(i+1))
print(answer)