def search(i, j):
    cnt[-1]+=1
    arr[i][j] = 2
    for k in range(4):
        newi, newj = i+dr[k], j+dc[k]
        if 0<=newi<N and 0<=newj<N and arr[newi][newj]==1:
            search(newi, newj)

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
dr = (1, -1, 0, 0)
dc = (0, 0, -1, 1)

cnt = []
for i in range(N):
    for j in range(N):
        if arr[i][j]==1:
            cnt.append(0)
            search(i, j)
if cnt:
    print(len(cnt))
    cnt.sort()
    for i in cnt: print(i)
else: print(0)
