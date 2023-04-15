import sys

input = sys.stdin.readline

M, N, L = map(int,input().split())

M_list = list(map(int,input().split()))

M_list.sort()

def binary_search(x):
    start = 0
    end = M - 1

    while start <= end:
        mid = (start + end) // 2
        if x == M_list[mid]:
            return mid
        elif x < M_list[mid]:
            end = mid - 1
        else:
            start = mid + 1
    
    return end

count = 0

for i in range(N):
    x, y = map(int,input().split())

    near_x_index = binary_search(x)

    print(near_x_index)

    dist = abs(x-M_list[near_x_index]) + y
    dist_right = abs(M_list[near_x_index+1]-x) + y if near_x_index < M-1 else float('inf')
    
    check = min(dist,dist_right)

    if check <= L:
        count +=1
    
    print(count)
print(count)