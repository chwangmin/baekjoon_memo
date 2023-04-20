from sys import stdin

input = stdin.readline

tree_num, tree_need = map(int,input().split())

tree_list = list(map(int,input().split()))
tree_list.sort()

left = 0
right = tree_list[-1]


while left <= right:
    mid = (left+right) // 2
    get_tree = 0
    for i in tree_list:
        get_tree += i-mid if i-mid > 0 else 0
    if get_tree >= tree_need:
        left = mid + 1
    else:
        right = mid - 1

print(right)