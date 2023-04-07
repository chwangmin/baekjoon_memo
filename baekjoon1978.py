import sys

num = int(sys.stdin.readline())

list_num = list(map(int,sys.stdin.readline().split()))

def prime_Check(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i+=1
    return True

count = 0

for i in list_num:
    if i > 1:
        if prime_Check(i):
            count+=1

print(count)