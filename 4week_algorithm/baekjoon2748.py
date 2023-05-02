import sys

input = sys.stdin.readline

num = int(input())

list_fibo = [0,1,1]

if num <= 2:
    print(list_fibo[num])

else:
    for i in range(2, num):
        x = list_fibo[i-1] + list_fibo[i]
        list_fibo.append(x)

    print(x)