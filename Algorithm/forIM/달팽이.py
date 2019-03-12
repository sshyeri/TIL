N = int(input())

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

s = [[0]*N for _ in range(N)]

r, c = 0, 0
k = 1
p = N-1
first = True
se = True
i, cnt = 0, 0

for _ in range(N*N):
    s[r][c] = k
    k += 1
    r += dr[i]
    c += dc[i]
    cnt+=1
    if cnt==p:
        cnt = 0
        i = (i+1)%4
        if first: first = False
        elif se: se = False
        elif not se:
            se = True
            p-=1

for i in s:
    print(*i)