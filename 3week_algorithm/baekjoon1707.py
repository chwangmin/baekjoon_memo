import sys

input = sys.stdin.readline

num = int(input())

for _ in range(num):
    a, b = map(int,input().split())

    tmp_index = [0] * ( a + 1 )

    check = True

    for _ in range(b):
        x, y = map(int,input().split())

        if x == y:
            check = False
        elif tmp_index[x] == 0 and tmp_index[y] == 0:
            tmp_index[x] = 1
            tmp_index[y] = 2
        elif tmp_index[x] == 1 and tmp_index[y] == 0:
            tmp_index[y] = 2
        elif tmp_index[x] == 2 and tmp_index[y] == 0:
            tmp_index[y] = 1
        elif tmp_index[y] == 1 and tmp_index[x] == 0:
            tmp_index[x] = 2
        elif tmp_index[y] == 2 and tmp_index[x] == 0:
            tmp_index[x] = 1
        else:
            check = False
    
    if check:
        print("YES")
    else:
        print("No")