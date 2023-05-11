import sys

input = sys.stdin.readline

num = int(input())

result = [[0,[]] for _ in range(num+1)] 

result[1][1] += [1]

for tmp_num in range(2, num + 1):
    result[tmp_num][0] = result[tmp_num-1][0] + 1
    result[tmp_num][1] = result[tmp_num-1][1] + [tmp_num]

    if tmp_num % 2 == 0 and result[tmp_num // 2][0] < result[tmp_num][0]:
        result[tmp_num][0] = result[tmp_num // 2][0] + 1
        result[tmp_num][1] = result[tmp_num // 2][1] + [tmp_num]
    if tmp_num % 3 == 0 and result[tmp_num // 3][0] < result[tmp_num][0]:
        result[tmp_num][0] = result[tmp_num // 3][0] + 1
        result[tmp_num][1] = result[tmp_num // 3][1] + [tmp_num]

print(result[num][0])
for i in range(result[num][0],-1,-1):
    print(result[num][1][i], end =' ')