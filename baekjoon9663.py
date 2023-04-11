import sys, time

num = int(sys.stdin.readline())

col = [0] * num

count = 0

def n_queen(n):
    global count 
    if n == num:
        count += 1
        return
    for i in range(1,num+1):
        col[n] = i
        if possible(n):
            n_queen(n+1)

def possible(n):
    for i in range(n):
        if col[n] == col[i] or abs(col[n]-col[i]) == n-i:
            return False
    return True

start = time.time()
n_queen(0)
print(count)
print(time.time()-start)