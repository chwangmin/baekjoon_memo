import sys

input = sys.stdin.readline

A, B, C = map(int,input().split())

def remainder(a,b,c):
    if b == 1:
        return a % c
    else:
        tmp = remainder(a ,b // 2, c)
        if b % 2 == 0:
            return (tmp * tmp) % c
        else:
            return (tmp * tmp * a) % c

print(remainder(A,B,C))


