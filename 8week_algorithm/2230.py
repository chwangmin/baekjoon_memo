import sys

sys.stdin = open('test.txt','r')

input = sys.stdin.readline

n, m = map(int,input().split())

num_list = []

for i in range(n):
    num_list.append(int(input()))

num_list.sort()

left = 0
right = 0

answer = sys.maxsize

while (1):
    if right >= n or left >= n:
        break
    if num_list[right] - num_list[left] < m:
        right += 1
    else:
        tmp_answer = num_list[right] - num_list[left]
        if tmp_answer < answer:
            answer = tmp_answer
        if answer == m:
            break
        left += 1

print(answer)
