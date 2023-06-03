import sys

sys.stdin = open('test.txt','r')

input = sys.stdin.readline

def first_B_check(tmp_map):
    change_num = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2:
                if tmp_map[i][j] != 'W':
                    change_num += 1
            else:
                if tmp_map[i][j] != 'B':
                    change_num += 1
    return change_num

def first_W_check(tmp_map):
    change_num = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2:
                if tmp_map[i][j] != 'B':
                    change_num += 1
            else:
                if tmp_map[i][j] != 'W':
                    change_num += 1
    return change_num

row, column = map(int,input().split())

input_map = [list(input().rstrip()) for _ in range(row)]

answer = 33

for i in range(row-8+1):
    for j in range(column-8+1):
        answer = min(answer, first_B_check([row[j:j+8] for row in input_map[i:i+8]]), first_W_check([row[j:j+8] for row in input_map[i:i+8]]))

print(answer)