import sys
 
input = sys.stdin.readline
 
n = int(input())
a = list(map(int,input().split()))
 
all =[]
def bf(arr, cur):
    if arr:
        for i in range(n-len(cur)):
            tmp = list(cur)
            tmp.append(arr[i])
            new_arr = arr[:i]+arr[i+1:]
            bf(new_arr, tmp)
    else:
        all.append(cur)
 
a = sorted(a)
bf(a,[])

ans = 0
for i in all:
    s = 0
    for j in range(1,n):
        s+=abs(i[j]-i[j-1])
    if ans<s:
        ans =s
print(ans)