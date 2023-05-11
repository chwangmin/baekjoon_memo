# https://velog.io/@hope1213/%EB%B0%B1%EC%A4%80-1149-RGB%EA%B1%B0%EB%A6%AC-%ED%8C%8C%EC%9D%B4%EC%8D%AC

n = int(input())
a = [0]*n

for i in range(n):
    a[i] = list(map(int,input().split()))
    
for i in range(1,n): # 1부터 시작하는 이유는 다음 입력값이 이전 입력값의 최소값을 사용하기때문이다
    a[i][0]= min(a[i-1][1],a[i-1][2]) + a[i][0]
    a[i][1]= min(a[i-1][0],a[i-1][2]) + a[i][1]
    a[i][2]= min(a[i-1][0],a[i-1][1]) + a[i][2]

print(min(a[n-1][0],a[n-1][1],a[n-1][2]))