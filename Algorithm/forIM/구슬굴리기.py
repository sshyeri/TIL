def iswall(r,c):
    return r<0 or c<0 or r>=R or c>=C or arr[r][c]==1

def search():
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 2:
                arr[i][j] = 3
                return (i, j)

C, R = map(int, input().split())
arr = [list(map(int, input())) for _ in range(R)]
N = int(input())
dir = list(map(int, input().split()))

dr = [0,-1,1,0,0]
dc = [0,0,0,-1,1]

cnt = 1
p = 0   #dir[p]

r, c = search()
while True:
    nr = r+dr[dir[p]]
    nc = c+dc[dir[p]]
    if iswall(nr, nc):
        p+=1
        if p>=N:
            break
    else:
        r = nr
        c = nc
        if arr[r][c]<1:
            cnt += 1
            arr[r][c] = 3


print(cnt)

