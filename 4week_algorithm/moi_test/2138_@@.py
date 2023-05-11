from sys import stdin as s


n = int(s.readline().strip())

arr=list(map(int,s.readline().strip()))
arr2=arr[:]

ans=list(map(int,s.readline().strip()))
answer=[]
count = 0

for i in range(2):
    cnt=0
    for i in range(count,len(arr)):
        
        if i == 0:
            if arr[i] == 0:
                arr[i]=1
            else:
                arr[i]=0
            if arr[i+1]==0:
                arr[i+1]=1
            else:
                arr[i+1]=0
            cnt+=1
        elif 0<i<len(arr)-1:
            if arr[i-1]==ans[i-1]:
                continue
            else:
                if arr[i-1]==1:
                    arr[i-1]=0
                else:
                    arr[i-1]=1
                if arr[i]==1:
                    arr[i]=0
                else:
                    arr[i]=1
                if arr[i+1]==1:
                    arr[i+1]=0
                else:
                    arr[i+1]=1
            cnt+=1
        else:
            if arr[i-1]==ans[i-1]:
                continue
            else:
                if arr[i-1]==1:
                    arr[i-1]=0
                else:
                    arr[i-1]=1
                if arr[i]==1:
                    arr[i]=0
                else:
                    arr[i]=1
            cnt+=1
    if ans==arr:
        answer.append(cnt)
            
    count+=1
    arr=arr2
    

if answer:
    print(min(answer))
else:
    print(-1)