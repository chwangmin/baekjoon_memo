import sys

input = sys.stdin.readline

def multi(a,b):
    if b == 1:
        return a % c
    else:
        tmp = multi(a,b//2)
        if b%2:
            return((tmp*tmp*a) % c)
        else:
            return((tmp*tmp) % c)

a,b,c = map(int,input().split())

print(multi(a,b))