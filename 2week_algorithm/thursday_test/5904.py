def func(length, mid_cnt, target_idx):
    prev_cnt = (length - mid_cnt) // 2

    if target_idx < prev_cnt: 
        return func(prev_cnt, mid_cnt - 1, target_idx)
    elif target_idx >= prev_cnt + mid_cnt: 
        return func(prev_cnt, mid_cnt - 1, target_idx - (prev_cnt + mid_cnt))
    else:
        return 'o' if target_idx - prev_cnt else 'm'

n = int(input())
length = 3
k = 3

while True:
    if length >= n:
        break
    k += 1
    length = 2 * length + k

# 몇 번째 글자를 원하니 인덱스는 -1 해주면 됨
# print(length, k, n - 1)
print(func(length, k, n - 1))