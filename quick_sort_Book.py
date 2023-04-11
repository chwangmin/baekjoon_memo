import sys, time

from typing import MutableMapping

def qsort(a: MutableMapping, left: int, right: int) -> None:
    pl = left
    pr = right
    x = a[(left+right) // 2]

    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    if left < pr: qsort(a, left, pr)
    if pl < right: qsort(a,pl,right)

def quick_sort(a:MutableMapping) -> None:
    qsort(a,0, len(a)-1)

x = list(map(int,sys.stdin.readline().split()))

start = time.time()
for i in range(100000):
    quick_sort(x)
print(time.time()-start)

print(x)