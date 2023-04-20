import sys

input = sys.stdin.readline

N, B = map(int,input().split())

matrix = [list(map(int,input().split()))for _ in range(N)]

def matrix_multi(n, matrix1, matrix2):
    result =[[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
            result[i][j] %= 1000
    return result

def devide(n, B, matrix):
    if B == 1:
        return matrix
    if B == 2:
        return matrix_multi(n, matrix, matrix)
    else:
        tmp = devide(n,B//2,matrix)
        if B % 2 == 0:
            return matrix_multi(n,tmp,tmp)
        else:
            return matrix_multi(n,matrix_multi(n,tmp,tmp),matrix)

answer = devide(N,B,matrix)

for i in range(N):
    for j in range(N):
        print(answer[i][j] % 1000, end=' ')
    print()