import sys

input = sys.stdin.readline

sniper_num, animal_num, sniper_range = map(int,input().split())

sinper_x = list(map(int,input().split()))
sinper_x.sort()

def left_near_x_check(x):
    left = 0
    right = sniper_num-1
    while left <= right:
        mid = (left + right) // 2
        if sinper_x[mid] <= x:
            left = mid + 1
        else:
            right = mid - 1
    return right

cnt = 0

for _ in range(animal_num):
    x, y = map(int,input().split())
    if y > sniper_range:
        continue
    nx = left_near_x_check(x)
    min1 = abs(x - sinper_x[nx]) + y
    min2 = sinper_x[nx+1] - x + y if nx < sniper_num-1 else sys.maxsize
    possible_check = min(min1,min2)
    if possible_check <= sniper_range:
        cnt +=1 

print(cnt)
