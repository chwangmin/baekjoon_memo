N = int(input())
N_li = list(map(int, input().split()))
M = int(input())
M_li = list(map(int,input().split()))

N_li.sort()

def binary_search(array, target, start, end):
    if start > end:
        return 0
    
    mid = (start+end) // 2

    if array[mid] == target:
        return 1
    if array[mid] > target:
        return binary_search(array,target,start,mid-1)
    if array[mid] < target:
        return binary_search(array, target, mid+1, end)
    
for i in M_li:
    print(binary_search(N_li, i, 0, N-1))


def binary_search2(array,target,start,end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
    return 0

for i in M_li:
    print(binary_search(N_li,i,0,N-1))