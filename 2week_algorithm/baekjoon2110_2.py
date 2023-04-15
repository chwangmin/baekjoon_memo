import sys

input = sys.stdin.readline

N, C = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()

start = 1 # 공유기 거리 최소
end = arr[-1] - arr[0] # 공유기 거리 최대
result = 0

while (start <= end):
    mid = (start+end) // 2
    value = arr[0]
    count = 1
    for i in range(1, len(arr)):
        if arr[i] >= value + mid:
            count += 1
            value = arr[i]
    if count >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)