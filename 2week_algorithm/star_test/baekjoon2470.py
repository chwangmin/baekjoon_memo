import sys

input = sys.stdin.readline

solution_num = int(input())

list_solution = list(map(int,input().split()))

list_solution.sort()

left = 0
right = solution_num-1
min = sys.maxsize

min_left = 0
min_right = solution_num-1

while left < right:
    mid = list_solution[left] + list_solution[right]
    abs_mid = abs(mid)
    if min > abs_mid:
        min_left = left
        min_right = right
        min = abs_mid
    if mid == 0:
        break
    elif mid > 0:
        right -=1
    else:
        left +=1

print(list_solution[min_left],list_solution[min_right])