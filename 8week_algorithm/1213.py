import sys

# A의 아스키코드는 65 Z의 아스키코드는 90

sys.stdin = open('test.txt','r')

input = sys.stdin.readline

list_alph = list(input().rstrip())

list_alph.sort()

list_alph_what = []
list_alph_num = [0] * 26

for alph in list_alph:
    list_alph_num[ord(alph)-65] += 1
    if alph not in list_alph_what:
        list_alph_what.append(alph)

odd_check = 0

for i in range(26):
    if list_alph_num[i] % 2 != 0:
        odd_check +=1
        odd_char = chr(i+65)

if odd_check <= 1:
    for i in range(26):
        for j in range(list_alph_num[i]//2):
            print(chr(i+65), end = '')
    if odd_check == 1:
        print(odd_char, end='')
    for i in range(25,-1,-1):
        for j in range(list_alph_num[i]//2):
            print(chr(i+65), end = '')
else:
    print("I'm Sorry Hansoo")