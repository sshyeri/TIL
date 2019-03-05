N = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

s = [[0]*N for _ in range(N)]

x, y = 0, 0
k = 1
p = N-1
first = True
se = True
i, c = 0, 0

for _ in range(N*N):
    s[x][y] = k
    k += 1
    x += dx[i]
    y += dy[i]
    c+=1
    if c==p:
        c = 0
        i = (i+1)%4
        if first: first = False
        elif se: se = False
        elif not se:
            se = True
            p-=1

for i in s:
    print(*i)