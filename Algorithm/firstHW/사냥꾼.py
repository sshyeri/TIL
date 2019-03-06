def iswall(r,c):
    return  r<0 or c<0 or r>=N or c>=N or not arr[r][c] or arr[r][c]==1
def hunt(r,c):
    global cnt
    for dir in range(8):
        for far in range(1,N):
            nr = r+far*dr[dir]
            nc = c+far*dc[dir]
            if iswall(nr, nc):
                break
            elif arr[nr][nc]==2:
                arr[nr][nc] = 3
                cnt += 1
    return cnt


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

dr = [-1,-1,-1,0,1,1,1,0]
dc = [-1,0,1,1,1,0,-1,-1]

cnt = 0
for r in range(N):
    for c in range(N):
        if arr[r][c]==1:
            hunt(r,c)
print(cnt)