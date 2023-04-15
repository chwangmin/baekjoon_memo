import sys

input = sys.stdin.readline

M, N, L = map(int,input().split())

M_list = list(map(int,input().split()))

M_list.sort()

def check_N(coo):
    if coo[1] > L:
        return 0
    left = 0
    right = M - 1

    result = 0

    if coo[0] > M_list[-1]:
        right -= 1
    
    else:
        while left <= right:
            mid = (left+right) // 2
            if M_list[mid] == coo[0]:
                return 1
            elif M_list[mid] < coo[0]:
                left = mid + 1
                result = mid
            else:
                right = mid - 1
                result = mid

    if 0 <= result < M and abs(coo[0] - M_list[result]) + coo[1] <= L:
        return 1
    if 0 <= result + 1 < M and abs(coo[0] - M_list[result + 1]) + coo[1] <= L:
        return 1
    if 0 <= result - 1 < M and abs(coo[0] - M_list[result - 1]) + coo[1] <= L:
        return 1
    return 0
    # if M_list[right+1] - coo[0] < coo[0] - M_list[right]:
    #     if coo[1] <= L - (M_list[right+1] - coo[0]):
    #         return 1
    #     else:
    #         return 0
    # else:
    #     if coo[1] <= L - (coo[0] - M_list[right]):
    #         return 1
    #     else:
    #         return 0
        
count = 0

for i in range(N):
    N_list = map(int,input().split())

    if check_N(N_list):
        count+=1

print(count)