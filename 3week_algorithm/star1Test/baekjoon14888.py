import sys

input = sys.stdin.readline

def dfs(i, result,plus,minus,multi,division):
    global max_num, min_num
    if i == num:
        max_num = max(max_num, result)
        min_num = min(min_num, result)

    if plus:
        dfs(i+1, result+list_num[i], plus-1, minus,multi,division)
    if minus:
        dfs(i+1, result-list_num[i], plus, minus-1 ,multi,division)
    if multi:
        dfs(i+1, result*list_num[i], plus, minus, multi-1, division)
    if division:
        dfs(i+1, int(result/list_num[i]), plus, minus,multi,division-1)

max_num = -sys.maxsize
min_num = sys.maxsize

num = int(input())

list_num = list(map(int,input().split()))

plus, minus, multi, division = map(int,input().split())

dfs(1, list_num[0], plus, minus, multi, division)

print(max_num)
print(min_num)