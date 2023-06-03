import sys

sys.stdin = open('test.txt','r')

input = sys.stdin.readline

def find_my_chair(student):
    possible_list = []
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(num):
        for j in range(num):
            if answer_matrix[i][j] == 0:
                priority_1 = 0
                priority_2 = 0
                for k in range(4):
                    nx = i+dx[k]
                    ny = j+dy[k]
                    if 0<=nx<num and 0<=ny<num:
                        if answer_matrix[nx][ny] in num_graph[student]:
                            priority_1+=1
                        if answer_matrix[nx][ny] == 0:
                            priority_2+=1
                possible_list.append([priority_1,priority_2,i,j])
    possible_list.sort(key=lambda x : (x[0],x[1],x[2],x[3]))
    answer_matrix[possible_list[0][x()]]

num = int(input())

num_graph = [[] for _ in range(num**2 + 1)]
answer_matrix = [[0]*num for _ in range(num)]

for i in range(num**2):
    tmp_list = list(map(int,input().split()))
    for i in range(1,5):
        num_graph[tmp_list[0]].append(tmp_list[i])

for i in range(1, num**9+1):
    find_my_chair(i)

        

print(num_graph)