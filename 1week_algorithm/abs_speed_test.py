## if 문을 쓰는 것이 abs 보다 4~5배 빠르다.

import time, math, sys

num = int(sys.stdin.readline())

def abs(num):
    for i in range(0, -1 * num, -1):
        abs(i)

start = time.time()
abs(num)
print(time.time()-start)

def if_abs(num):
    for i in range(0, -1 * num, -1):
        if i < 0:
            i = -1 * i

start = time.time()
if_abs(num)
print(time.time()-start)