import sys

input = sys.stdin.readline

check_color = 1

def dfs(x):
    global check_color
    global color_index
    print(x)
    print(color_index)
    color_index[x] = check_color
    print(x)
    if check_color == 1:
        check_color = 2
    else:
        check_color = 1
    for i in tmp_index[x]:
        if color_index[i] == 0:
            color_index = check_color
        elif color_index[i] != check_color:
            global check
            check = False
            break
        dfs(i)

num = int(input())

for _ in range(num):
    a, b = map(int,input().split())

    tmp_index = [[] * (a+1) for _ in range(a+1)]
    color_index = [0] * (a+1)
    print(color_index)

    check = True

    for _ in range(b):
        x, y = map(int,input().split())

        tmp_index[x].append(y)
        tmp_index[y].append(x)

    print(tmp_index)

    dfs(1)
    
    if check:
        print("YES")
    else:
        print("No")