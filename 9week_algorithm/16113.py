import sys

sys.stdin = open('test.txt','r')

input = sys.stdin.readline

num = int(input())

list_char = list(input().rstrip())

divide = num // 5

map_answer = list()

for i in range(divide, num+1, divide):
    map_answer.append(list_char[i-divide:i])

cnt_continue = 0

for i in range(divide):
    if cnt_continue:
        cnt_continue -= 1
        continue
    if map_answer[0][i] == '#' and map_answer[1][i] == '#' and map_answer[2][i] == '#' and map_answer[3][i] == '#' and map_answer[4][i] == '#':
        if i+1 < divide:
            if map_answer[0][i+1] == '#' and map_answer[1][i+1] == '.' and map_answer[2][i+1] == '.' and map_answer[3][i+1] == '.' and map_answer[4][i+1] == '#':
                if map_answer[0][i+2] == '#' and map_answer[1][i+2] == '#' and map_answer[2][i+2] == '#' and map_answer[3][i+2] == '#' and map_answer[4][i+2] == '#':
                    print(0,end='')
                    cnt_continue+=2
            if map_answer[0][i+1] == '.' and map_answer[1][i+1] == '.' and map_answer[2][i+1] == '.' and map_answer[3][i+1] == '.' and map_answer[4][i+1] == '.':
                print(1,end='')
                cnt_continue+=1
            if map_answer[0][i+1] == '#' and map_answer[1][i+1] == '.' and map_answer[2][i+1] == '#' and map_answer[3][i+1] == '.' and map_answer[4][i+1] == '#':
                if map_answer[0][i+2] == '#' and map_answer[1][i+2] == '.' and map_answer[2][i+2] == '#' and map_answer[3][i+2] == '#' and map_answer[4][i+2] == '#':
                    print(6,end='')
                    cnt_continue+=2
            if map_answer[0][i+1] == '#' and map_answer[1][i+1] == '.' and map_answer[2][i+1] == '#' and map_answer[3][i+1] == '.' and map_answer[4][i+1] == '#':
                if map_answer[0][i+2] == '#' and map_answer[1][i+2] == '#' and map_answer[2][i+2] == '#' and map_answer[3][i+2] == '#' and map_answer[4][i+2] == '#':
                    print(8,end='')
                    cnt_continue+=2
        else:
            print(1,end='')
            cnt_continue+=1
    if map_answer[0][i] == '#' and map_answer[1][i] == '.' and map_answer[2][i] == '#' and map_answer[3][i] == '#' and map_answer[4][i] == '#':
        if i < divide:
            if map_answer[0][i+1] == '#' and map_answer[1][i+1] == '.' and map_answer[2][i+1] == '#' and map_answer[3][i+1] == '.' and map_answer[4][i+1] == '#':
                if map_answer[0][i+2] == '#' and map_answer[1][i+2] == '#' and map_answer[2][i+2] == '#' and map_answer[3][i+2] == '.' and map_answer[4][i+2] == '#':
                    print(2,end='')
                    cnt_continue+=2
    if map_answer[0][i] == '#' and map_answer[1][i] == '.' and map_answer[2][i] == '#' and map_answer[3][i] == '.' and map_answer[4][i] == '#':
        if i < divide:
            if map_answer[0][i+1] == '#' and map_answer[1][i+1] == '.' and map_answer[2][i+1] == '#' and map_answer[3][i+1] == '.' and map_answer[4][i+1] == '#':
                if map_answer[0][i+2] == '#' and map_answer[1][i+2] == '#' and map_answer[2][i+2] == '#' and map_answer[3][i+2] == '#' and map_answer[4][i+2] == '#':
                    print(3,end='')
                    cnt_continue+=2
    if map_answer[0][i] == '#' and map_answer[1][i] == '#' and map_answer[2][i] == '#' and map_answer[3][i] == '.' and map_answer[4][i] == '.':
        print(4,end='')
        cnt_continue+=2
    if map_answer[0][i] == '#' and map_answer[1][i] == '#' and map_answer[2][i] == '#' and map_answer[3][i] == '.' and map_answer[4][i] == '#':
         if i < divide :
            if map_answer[0][i+1] == '#' and map_answer[1][i+1] == '.' and map_answer[2][i+1] == '#' and map_answer[3][i+1] == '.' and map_answer[4][i+1] == '#':
                    if map_answer[0][i+2] == '#' and map_answer[1][i+2] == '.' and map_answer[2][i+2] == '#' and map_answer[3][i+2] == '#' and map_answer[4][i+2] == '#':
                        print(5,end='')
                        cnt_continue+=2
            if map_answer[0][i+1] == '#' and map_answer[1][i+1] == '.' and map_answer[2][i+1] == '#' and map_answer[3][i+1] == '.' and map_answer[4][i+1] == '#':
                    if map_answer[0][i+2] == '#' and map_answer[1][i+2] == '#' and map_answer[2][i+2] == '#' and map_answer[3][i+2] == '#' and map_answer[4][i+2] == '#':
                        print(9,end='')
                        cnt_continue+=2
    if map_answer[0][i] == '#' and map_answer[1][i] == '.' and map_answer[2][i] == '.' and map_answer[3][i] == '.' and map_answer[4][i] == '.':
        print(7,end='')
        cnt_continue+=2