N = int(input())
N_li = list(map(int, input().split()))
M = int(input())
M_li = list(map(int,input().split()))

N_li.sort()

def binary_search(x, left, right):
    mid = (left + right) // 2

    if left > right:
        return 0
    if N_li[mid] == x:
        return 1
    elif N_li[mid] > x:
        return binary_search(x, left, mid-1)
    elif N_li[mid] < x:
        return binary_search(x, mid+1 ,right)

for i in M_li:
    print(binary_search(i,0,N-1))