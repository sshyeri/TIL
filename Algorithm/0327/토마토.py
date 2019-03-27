C, R = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(R)]

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

tomato = []
for r in range(R):
    for c in range(C):
        if box[r][c]==1:
            tomato.append((r, c))
if len(tomato)==R*C: print(0)
else:
    while tomato:
        r, c = tomato.pop(0)
        for i in range(4):
            newr, newc = r+dr[i], c+dc[i]
            if 0<=newr<R and 0<=newc<C and box[newr][newc]==0:
                box[newr][newc] = box[r][c] + 1
                tomato.append((newr,newc))
    for to in box:
        if to.count(0):
            print(-1)
            break
    else: print(box[r][c]-1)
