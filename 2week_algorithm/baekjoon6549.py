import sys

def max_square(l, r):
    if l == r:
        return h[l]
    else:
        m = (l + r) // 2
        nl = m
        nr = m + 1
        nh = min(h[nl], h[nr])
        tmp = nh * 2

        cnt = 2
        while True:
            if (h[nl] == 0 or nl == l) and (h[nr] == 0 or nr == r): 
                break
            elif h[nl] == 0 or nl == l:
                if h[nr + 1] < nh:
                    nh = h[nr + 1]
                nr += 1
            elif h[nr] == 0 or nr == r:
                if h[nl - 1] < nh:
                    nh = h[nl - 1]
                nl -= 1
            else:
                if h[nl - 1] > h[nr + 1]:
                    if h[nl - 1] < nh:
                        nh = h[nl - 1]
                    nl -= 1
                else:
                    if h[nr + 1] < nh:
                        nh = h[nr + 1]
                    nr += 1
            cnt += 1
            tmp = max(tmp, nh * cnt)
        return(max(max_square(l, m), max_square(m + 1, r), tmp))  

while True:
    h = list(map(int, sys.stdin.readline().split()))
    if h[0] == 0:
        break
    print(max_square(1, len(h) - 1))

# https://velog.io/@piopiop/%EB%B0%B1%EC%A4%80-6549-%ED%9E%88%EC%8A%A4%ED%86%A0%EA%B7%B8%EB%9E%A8%EC%97%90%EC%84%9C-%EA%B0%80%EC%9E%A5-%ED%81%B0-%EC%A7%81%EC%82%AC%EA%B0%81%ED%98%95%ED%8C%8C%EC%9D%B4%EC%8D%AC