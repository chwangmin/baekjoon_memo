import sys

num = sys.stdin.readline()

x = list(map(int,sys.stdin.readline().split()))

count = 0

def sosu(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i +=1
    return True

for i in x:
    if i > 1:
        if sosu(i):
            count += 1

print(count)