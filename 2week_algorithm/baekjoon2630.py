import sys
input = sys.stdin.readline

color_check=[]

def check_color(x,y,N):
    first_color = color_paper_list[x][y]
    for i in range(x,x+N):
        for j in range(y,y+N):
            if color_paper_list[i][j] != first_color:
                check_color(x,y,N//2)
                check_color(x+N//2,y,N//2)
                check_color(x,y+N//2,N//2)
                check_color(x+N//2,y+N//2,N//2)
                return
    if first_color == 0:
        color_check.append(0)
    else:
        color_check.append(1)

N = int(input())
color_paper_list = [list(map(int,input().split()))for _ in range(N)]

check_color(0,0,N)

print(color_check.count(0))
print(color_check.count(1))
