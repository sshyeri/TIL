def depth(r, c):
    for d in range(1, N):
        for k in range(4):
            nr = r+d*dr[k]
            nc = c+d*dc[k]
            if not pond[nr][nc]:
                return d
N = int(input())
pond = [list(map(int, input().split())) for _ in range(N)]

dr = [1,-1,0,0]
dc = [0,0,1,-1]

cnt = 0
for i in range(N):
    for j in range(N):
        if pond[i][j]:
            cnt += depth(i, j)

print(cnt)