num = int(input())

a = list(map(int,input().split()))

def _merge_sort(a, left, right):
    if left < right:
        center = (left + right) // 2

        _merge_sort(a,left,center)
        _merge_sort(a,center+1,right)

        p = j = 0
        i = k = left
        while i <= center:
            buff[p] = a[i]
            p+= 1
            i+= 1

        while i <= right and j < p:
            if buff[j] >= a[i]:
                a[k] = buff[j]
                j+=1
            else:
                a[k] = a[i]
                i+=1
            k+=1

        while j < p:
            a[k] = buff[j]
            k+=1
            j+=1

buff = [None] * num
_merge_sort(a,0,num-1)
print(a)
