def iswall(r,c):
    return r<0 or c<0 or r>=N or c>=N or arr[r][c]==1

dr=[0, 1,0,-1,0]
dc=[0, 0,-1,0,1]

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
d = list(map(int, input().split()))

r, c, p, cnt = 0, 0, 0, 0
while True:

    nr = r+dr[d[p]]
    nc = c+dc[d[p]]
    if iswall(nr, nc):
        p = (p+1)%4
    elif arr[nr][nc]==2:
        break
    else:
        r = nr
        c = nc
        arr[r][c] = 2
        cnt += 1

print(cnt)