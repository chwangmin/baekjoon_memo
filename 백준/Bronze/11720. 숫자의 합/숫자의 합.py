import sys

input = sys.stdin.readline

num_check = int(input())
num_list = input().rstrip()

result = 0

for i in num_list:
    result += int(i)

print(result)