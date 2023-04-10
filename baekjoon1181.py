import sys

num = int(sys.stdin.readline())

list_ch = []

for i in range(num):
    list_ch.append(sys.stdin.readline().strip())

list_ch = set(list_ch)
list_ch = list(list_ch)
list_ch.sort()
list_ch.sort(key=len)

for i in list_ch:
    print(i)
