import sys

input = sys.stdin.readline

num, squre_num = map(int,input().split())

matrix = [list(map(int,input().split())) for _ in range(num)]

def matrix_multifly(n, matrix1, matrix2):
    result = [[0 for _ in range(num)] for _ in range(num)]
    for i in range(num):
        for j in range(num):
            for k in range(num):
                result[i][j] += matrix1[k][i] * matrix2[j][k]
            result[i][j] %= 1000
    return result

def devide(n,b,matrix):
    if b == 1:
        return matrix
    elif b == 2:
        return matrix_multifly(n,matrix,matrix)
    else:
        tmp = devide(n,b//2,matrix)
        if b % 2 == 0:
            return matrix_multifly(n,tmp,tmp)
        else:
            return matrix_multifly(n,matrix_multifly(n,tmp,tmp),matrix)
        
result = devide(num,squre_num,matrix)

for row in result:
    for num in row:
        print(num % 1000, end =' ')
    print()