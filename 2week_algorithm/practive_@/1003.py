import sys

input = sys.stdin.readline

num = int(input())

ch_zero = [0] * 41
ch_one = [0] * 41

ch_zero[0] = 1
ch_one[1] = 1

for i in range(2, 41):
    ch_zero[i] += ch_zero[i-2] + ch_zero[i-1]
    ch_one[i] += ch_one[i-1] + ch_one[i-2]
        

for i in range(num):
    x = int(input())
    print(ch_zero[x], ch_one[x])