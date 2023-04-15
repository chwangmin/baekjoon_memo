n = int(input())
arr = list(map(int, input().split(' ')))
arr.sort()

left = 0
right = n-1

check = abs(arr[right] + arr[left])
ch_left = arr[0]
ch_right = arr[-1]

while left < right:
    result = arr[right] + arr[left]
    if abs(result) < check:
        check = abs(result)
        ch_left = arr[left]
        ch_right = arr[right]
        if check == 0:
            break
    if result < 0:
        left += 1
    else:
        right -= 1

print(ch_left, ch_right)