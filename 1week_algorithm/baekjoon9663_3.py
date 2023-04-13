import sys

num = int(sys.stdin.readline())

flag_a = [False] * num
flag_b = [False] * (num*2-1)
flag_c = [False] * (num*2-1)

count = 0

def n_queen(n):
    global count
    if n == num:
        count+=1
    for i in range(num):
        if not flag_a[i] and not flag_b[i+n] and not flag_c[i-n+num-1]:
            flag_a[i] = flag_b[n+i] = flag_c[i-n+num-1] = True
            n_queen(n+1)
            flag_a[i] = flag_b[n+i] = flag_c[i-n+num-1] = False

n_queen(0)

print(count)