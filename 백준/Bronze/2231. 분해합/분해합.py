import sys

input = sys.stdin.readline

num = int(input())

for i in range(1,num+1):
    part_sum = sum(map(int,str(i)))
    check_num = i + part_sum
    
    if check_num == num:
        print(i)
        break
    if i == num:
        print(0)