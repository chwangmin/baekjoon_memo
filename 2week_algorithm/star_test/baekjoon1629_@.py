import sys

input = sys.stdin.readline

A, B, C = map(int,input().split())

def devide(A,B,C):
    if B == 1:
        return A % C
    else:
        tmp = devide(A,B//2,C)
        if B % 2 == 0:
            return (tmp * tmp) % C
        else:
            return (tmp * tmp * A) % C

print(devide(A,B,C))