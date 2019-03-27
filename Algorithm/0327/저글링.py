C, R  = map(int, input().split())
arr = [list(map(int, input())) for _ in range(R)]
c1, r1 = map(lambda x:int(x)-1, input().split())
dr = (1, -1, 0, 0)
dc = (0, 0, -1, 1)
Q=[(r1,c1)]
arr[r1][c1] = 3
while Q:
    r, c = Q.pop(0)
    for i in range(4):
        newr, newc = r+dr[i], c+dc[i]
        if 0<=newr<R and 0<=newc<C and arr[newr][newc]==1:
            Q.append((newr,newc))
            arr[newr][newc] += arr[r][c]
print(arr[r][c])
cnt = 0
for i in arr: cnt += i.count(1)
print(cnt)