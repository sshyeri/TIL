C, R = map(int, input().split())
c1, r1, c2, r2 = map(lambda x:int(x)-1, input().split())
arr = [list(map(int,input())) for _ in range(R)]
Q = [(r1, c1)]
dr = (1, -1, 0, 0)
dc = (0, 0, -1, 1)
while Q:
    r, c = Q.pop(0)
    for i in range(4):
        newr, newc = r+dr[i], c+dc[i]
        if 0<=newr<R and 0<=newc<C and not arr[newr][newc]:
            Q.append((newr,newc))
            arr[newr][newc] = arr[r][c] + 1
    if arr[r2][c2]: break
print(arr[r2][c2])

