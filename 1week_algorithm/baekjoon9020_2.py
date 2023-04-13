import sys

def prime_list(n) -> None:
    m = int(n ** 0.5)

    for i in range(2, m+1):
        if a[i] == True:
            for j in range(i+i, n, i):
                a[j] = False

n = int(sys.stdin.readline())
a = [True] * 10000

prime_list(10000)

for i in range(n):
    x = int(sys.stdin.readline())

    for j in range(x//2,x):
        if a[j] == True:
            if a[x-j] == True:
                print(x-j, j)
                break
